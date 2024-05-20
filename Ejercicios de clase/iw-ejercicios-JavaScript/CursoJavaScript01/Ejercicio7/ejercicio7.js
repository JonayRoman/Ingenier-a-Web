/* Crea un programa que muestre el resultado de la suma de todos los números del 20 al 50. */
let num_inicial = 20;
let total = 0;
do {
    total = total + num_inicial;
    num_inicial++;
    alert(num_inicial)
} while (num_inicial < 50)
alert(total);