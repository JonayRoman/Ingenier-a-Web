/* Crea una página HTML y cambia el color de fondo del cuerpo de la página (body) utilizando JS */
document.body.style.backgroundColor = "red";

/* Realiza las siguientes operaciones en el código HTML dado a continuación:
    ■ Selecciona el elemento h2 de la página y cambia su color de texto a blue
    ■ Establece la propiedad font-weight a 700 en los elementos de clase “importante”.  */
let elementoH2 = document.getElementsByTagName("h2");
for (let elemento1 of elementoH2) {
    elemento1.style.color="blue";
}
let classImportante = document.querySelectorAll(".importante");
for (let elemento of classImportante) {
    elemento.style.fontWeight = 700;
}

