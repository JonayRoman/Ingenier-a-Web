/*Selecciona el elemento con id “titular” y muestra su contenido en la consola
mediante la propiedad textContent.*/ 
let elemento =  document.getElementById('titular');
console.log(elemento.textContent);

/*Selecciona todos los elementos con clase “importante” y muestra su contenido
por la consola.*/ 
let elementos = document.getElementsByClassName('importante');
for (let elementoSingular of elementos) {
    console.log(elementoSingular.textContent);
}


