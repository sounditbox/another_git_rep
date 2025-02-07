const socket = new WebSocket('ws://localhost:80');
socket.onopen = function(event) {
    console.log('Соединение установлено');
    socket.send(JSON.stringify({'type': 'join'}));
}
socket.onclose = function(event) {
    socket.send(JSON.stringify({'type': 'leave'}));
    console.log('Соединение закрыто', event.code, event.reason);
}
socket.onerror = function(event) {
    console.error('Ошибка:', event);
}
socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    if (data['type'] == 'join'){
        console.log('Пользователь присоединился');
        document.getElementById('usersCount').textContent = data['users_count'];
    }
    else if (data['type'] == 'message'){
        addMessage(data['message']);
        console.log(data['message']);
    }
    else if (data['type'] == 'leave'){
        document.getElementById('usersCount').textContent = data['users_count'];
    }
    else if (data['type'] == 'update'){
        for (let item of data['messages']){
            addMessage(item);
        }
    }
}
document.getElementById('send').addEventListener('click', sendMessage);
function sendMessage() {
    let elem = document.getElementById('message');
    socket.send(JSON.stringify({'type': 'message', 'message': message.value}));
    elem.value = '';
}

function addMessage(message) {
    console.log('Новое сообщение: ' + message)
    let chat = document.getElementById('chat');
    let li = document.createElement('li');
    li.textContent = message;
    chat.appendChild(li);
}