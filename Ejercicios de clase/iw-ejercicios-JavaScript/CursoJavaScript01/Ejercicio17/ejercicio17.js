/* Crea un objeto llamado inversiones que contenga las siguientes propiedades:
■ fondos: con valor de 300
■ oro: con valor de 400
Crea una función que reciba el objeto y un número entero por el cual tendrá que multiplicar todos los valores 
del objeto. Por ejemplo, si el número es 2, fondos tendrá un valor de 600 y oro tendrá un valor de 800 */

let inversiones = {
    fondos: 300,
    oro: 400
};

let num = parseInt(prompt("Escribe un número:"))
alert(inversionActualizado(inversiones, num));

function inversionActualizado (objeto, numero) {
    for (elemento in objeto) {
        objeto[elemento] *= numero;
    }
    return objeto;
}