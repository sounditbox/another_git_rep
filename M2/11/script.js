function myFunc() {
    // Обновление содержимого параграфа
    let btn = document.querySelector('button');
    btn.onclick = myFunc2;
    btn.textContent = 'Нажми ещё раз!';
    const paragraph = document.querySelector('p'); // Выбор первого параграфа
    paragraph.textContent = 'Новый текст параграфа'; // Замена текста параграфа
    // Создание нового элемента и добавление его на страницу
    const newDiv = document.createElement('div'); // Создание нового div элемента
    newDiv.className = 'new-class'; // Добавление класса к новому div элементу
    newDiv.id = 'div-to-del'
    newDiv.textContent = 'Это новый элемент'; // Добавление текста
    document.body.appendChild(newDiv); // Добавление div к body
    for (let c of document.getElementsByClassName('new-class')) {
        console.log(c);
    }

}

function myFunc2() {
    let btn = document.querySelector('button');
    btn.onclick = myFunc;
    btn.textContent = 'Нажми на меня!';
    document.getElementById('div-to-del').remove();
}

function myFunc3() {
    // Создаем элемент и устанавливаем атрибуты
    const image = document.getElementById('img');
    image.setAttribute('src', 'image.jpg');
    image.setAttribute('alt', 'Картинка не найдена');
    image.setAttribute('width', '480');
    image.height = '270';
}

function myFunc4() {

    // Получаем ссылку на элемент
    const myElement = document.getElementById("myId");
    // Изменяем цвет фона
    myElement.style.backgroundColor = "red";
    // Добавляем класс
    myElement.classList.add("bordered");
    myElement.style.border = 'solid';
    myElement.style.borderColor = 'green';

    myElement.style.borderWidth = "12px";
}
// Выбираем кнопку
const button = document.getElementById('myButton');
// Добавляем обработчик клика
button.addEventListener('click', function() {
alert('Кнопка нажата!');
});
