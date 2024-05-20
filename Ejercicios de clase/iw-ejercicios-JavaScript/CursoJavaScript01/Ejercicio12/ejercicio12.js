/*  Escribe una función sumarConInteres que sume dos cantidades y aplique un interés al resultado. Para 
cualquier suma menor o igual a 10, tendrá que sumarle un interés de 1. Para cada cantidad mayor que 10, 
el interés a sumar será 2. Por ejemplo, la llamada sumarConInteres (5, 3) devolverá 9 y la llamada a
sumarConInteres(7,9) devolverá 18. */

let num_1 = parseFloat(prompt("Escribe el primer número:"));
let num_2 = parseFloat(prompt("Escribe el segundo número:"));

sumarConInteres(num_1, num_2);
sumarConInteres(5, 3);
sumarConInteres(7, 9);

function sumarConInteres (num1, num2) {
    let suma = num1 + num2;
    if (suma <= 10) {
        suma = suma + 1;
        alert(suma);
    } else {
        suma += 2;
        alert(suma);
    }
}