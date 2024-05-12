/* Crea la función esPar que reciba un número y saque una alerta diciendo si el número es par o impar. */
let numero = prompt("Escribe un número: ");

function esPar (num) {
    if (num % 2 == 0) {
        return(alert(`El número ${num} es un número par`));
    } else {
        return(alert(`El número ${num} es un número impar`));
    }
}

esPar(numero);