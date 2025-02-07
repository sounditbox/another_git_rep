const parentList = document.getElementById('parentList');
parentList.addEventListener('click', (event) => {
    if (event.target && event.target.matches('li.item')) {
    console.log(`Clicked on item: ${event.target.textContent}`);
    }
});
