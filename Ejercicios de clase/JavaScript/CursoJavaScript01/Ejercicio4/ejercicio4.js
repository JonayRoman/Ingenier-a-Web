/* Crea una página que evalúe si el valor de una variables es mayor, igual o menor que 18. En caso de ser igual 
o mayor mostrará el mensaje: “Ya puedes votar”, en caso de ser menor, mostrará cuántos años le quedan para 
votar. Por ejemplo, en caso de ser 15, mostrará el mensaje: “Todavía te quedan 3 años para votar”. */
let edad = 1;

if (edad >= 18) {
    alert("Ya puedes votar.");
} else {
    let años_hasta_votar = 18 - edad;
    alert(`Todavía te quedan ${años_hasta_votar} años para votar.`)
}