let socket = new WebSocket("ws://localhost:8765");
socket.onopen = function(event) {
    console.log('Соединение установлено');
    socket.send('Привет, сервер!');
};
socket.onmessage = function(event) {
    let mes = document.createElement('p');
    mes.textContent = event.data + '\t-\t' + new Date();
    mes.align = 'left';
    mes.style.color = 'green';
    document.getElementById('chat').appendChild(mes);
};
socket.onerror = function(event) {
    console.error('Ошибка:', event);
};
socket.onclose = function(event) {
    console.log('Соединение закрыто');
};

document.getElementById('send').addEventListener('click', () => {

    let mes = document.createElement('p');
    mes.align = 'right';
    mes.style.color = 'blue';
    let input = document.getElementById('message');
    mes.textContent = input.value + '\t-\t' + new Date();
    document.getElementById('chat').appendChild(mes);
    socket.send(input.value);
    input.value = '';
});
