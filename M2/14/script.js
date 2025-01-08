console.log("Начало");
// Макрозадача 1: setTimeout
setTimeout(() => {
    console.log("setTimeout");
    // Микрозадача 1, вложенная в макрозадачу 1
    Promise.resolve()
        .then(() => console.log("Promise.then внутри setTimeout"));
    // Макрозадача 2, вложенная в макрозадачу 1
    setTimeout(() => {
        console.log("Вложенный setTimeout");
        }, 0);
    }, 0);
// Микрозадача 2
Promise.resolve()
    .then(() => console.log("Promise.then"));
console.log("Конец");