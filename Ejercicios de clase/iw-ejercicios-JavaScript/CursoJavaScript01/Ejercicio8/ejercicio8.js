/* Crea un programa que itere por los números del 1 al 20 y muestre por pantalla únicamente los números pares.
Nota: utiliza la función console.log() para mostrar los números en la consola del navegador. */
let num_inicial = 1;

do {
    if (num_inicial % 2 == 0) {
        console.log(num_inicial);
    }
    num_inicial++;
} while (num_inicial < 20)