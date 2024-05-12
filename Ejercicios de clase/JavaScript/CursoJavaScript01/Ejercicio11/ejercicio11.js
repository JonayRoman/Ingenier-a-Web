/* Crea una función llamada saludar que reciba un nombre y muestre mediante una alerta un saludo. En caso de 
no recibir especificar ningún parámetro, utilizará como nombre la palabra anónimo. Algunos ejemplos:
● saludar(“Aritz”) → Hola, Aritz
● saludar(“Izaro”) → Hola, Izaro
● saludar() → Hola, anónimo*/
let nombre = prompt("¿Cuál es tu nombre?");

function saludar (persona) {
    if (persona) {
        alert(`Hola, ${persona}`);
    } else {
        alert("Hola anónimo");
    }
}

saludar(nombre);
saludar("Izaro");
saludar();