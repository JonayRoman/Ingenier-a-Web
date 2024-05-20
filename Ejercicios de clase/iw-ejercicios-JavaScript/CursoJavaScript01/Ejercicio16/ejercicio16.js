/* Crea un objeto llamado cuentaCorriente que contenga las siguientes propiedades:
■ saldoInicial: con valor de 1500
■ compras: con valor de -300
■ alquiler: con valor de -800
Crea una función que reciba el objeto y utilizando un bucle calcule la suma de los valores de las propiedades 
del objeto. En el ejemplo devolverá 400 (resultado de 1500-300-800). */
let cuentaCorriente = {
    saldoInicial: 1500,
    compras: -300,
    alquiler: -800
};

console.log(dineroFinal(cuentaCorriente));

function dineroFinal (objeto) {
    let dineroTotal = 0;
    for (elemento in objeto) {
        dineroTotal += objeto[elemento];
    }
    return dineroTotal;
}