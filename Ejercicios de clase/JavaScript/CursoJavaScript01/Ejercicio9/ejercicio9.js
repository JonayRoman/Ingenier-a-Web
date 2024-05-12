/* Crea una función que reciba dos strings y muestre en un alert la concatenación de ambos.. */
let string_1 = prompt("Escribe una frase");
let string_2 = prompt("Escribe otra frase");

function concatenar_strings (frase1, frase2) {
    let frase = frase1 + " " + frase2;
    return frase;
}

alert(concatenar_strings(string_1, string_2));