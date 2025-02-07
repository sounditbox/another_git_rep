const websocket = new WebSocket('ws://localhost:8000/ws');

const chat = document.getElementById('chat');
const input = document.getElementById('message');
const button = document.getElementById('send');
const versionsList = document.getElementById('versions');

button.addEventListener('click', () => {
    if (!input.value == '') {
        addMessage(input.value, 'user');
        websocket.send(input.value);
        input.value = '';
    }
});



websocket.onopen = function(event) {
    console.log('Соединение установлено');
};

websocket.onmessage = function(event) {
    addMessage(event.data, 'bot');
};

websocket.onerror = function(event) {
    console.error("WebSocket Error:", event);
};

websocket.onclose = function(event) {
    console.warn("WebSocket Closed:", event);
};

const botClassList = ['d-flex', 'flex-row', 'justify-content-end', 'mb-4', 'pt-1'];
const userClassList = ['d-flex', 'flex-row', 'justify-content-start', 'mb-4'];
const botImgSrc = 'https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png';
const userImgSrc = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp';
const botMsgClassList = ['small', 'p-2', 'ms-3', 'mb-1', 'rounded-3', 'bg-body-tertiary']
const userMsgClassList = ['small', 'p-2', 'me-3', 'mb-1', 'text-white', 'rounded-3', 'bg-primary']
const botVersionButton = document.getElementById('botVersion');


function addMessage(text, sender) {
    let messageContainer = document.createElement('div');
    messageContainer.classList.add(...(sender == 'user' ? userClassList : botClassList));

    let img = document.createElement('img');
    img.src = sender == 'user' ? userImgSrc : botImgSrc;
    img.alt = 'avatar';
    img.style.width = '45px';
    img.style.height = '100%';

    let mesDiv = document.createElement('div');


    let mes = document.createElement('p');
    mes.classList.add(...(sender == 'user' ? userMsgClassList : botMsgClassList));
    mes.textContent = text;

    let ts = document.createElement('p');
    ts.classList.add('small', 'ms-3', 'mb-3', 'rounded-3', 'text-muted');
    let now = new Date();
    ts.textContent = now.getHours() + ':' + now.getMinutes();

    if (sender == 'user') {
        messageContainer.appendChild(img);
    }

    mesDiv.appendChild(mes);
    mesDiv.appendChild(ts);
    messageContainer.appendChild(mesDiv);

    if (sender == 'bot') {
        messageContainer.appendChild(img);
    }

    chat.appendChild(messageContainer);
}



function changeVersion(newVersion) {
    fetch('http://127.0.0.1:8000/set_version', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ version: newVersion })
    })
    .then(response => {
        if (!response.ok) throw new Error(`Ошибка: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log("Версия успешно изменена:", data);
        botVersionButton.innerText = newVersion;
        document.querySelectorAll('.dropdown-item').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelector(`.dropdown-item[data-version="${newVersion}"]`).classList.add('active');
    })
    .catch(error => console.error("Ошибка при смене версии:", error));
}

fetch('http://127.0.0.1:8000/versions')
    .then(response => {
        if (!response.ok) throw new Error(`Ошибка: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log("Ответ сервера:", data);
        if (!data.versions) throw new Error("Поле 'versions' отсутствует в ответе сервера");

        data.versions.forEach((item, index) => {
            let li = document.createElement('li');
            let a = document.createElement('a');

            a.classList.add('dropdown-item');
            a.href = "#";
            a.innerText = item;
            a.dataset.version = item;
            if (index === 0) {
                a.classList.add('active');
            }
            a.addEventListener('click', (event) => {
                event.preventDefault();
                changeVersion(item);
            });

            li.appendChild(a);
            versionsList.appendChild(li);
        });
    })
    .catch(error => {
        console.error("Ошибка запроса:", error);
    });
