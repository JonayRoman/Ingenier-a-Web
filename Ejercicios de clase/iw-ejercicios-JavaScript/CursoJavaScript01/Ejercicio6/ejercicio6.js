/* Crea un programa que añada puntos (‘.’) al final de un string hasta que la longitud de ese string sea 30. 
Si la longitud es mayor que 30 no hará nada. Finalmente lo mostrará por pantalla.
Ejemplo: si el string es “casa”, el resultado será: “casa............................” */
let string = prompt("Escribe una frase");

do {
    string += ".";

} while (string.length < 30)
    
alert(string)