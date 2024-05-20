/* Genera una lista HTML con los datos de un objeto como el siguiente: */
const estudiante = {
    nombre : 'Amaia',
    apellidos : 'Jainaga Urrutia',
    edad : 27,
    email : 'amaia@email.com'
}

let lista = document.createElement('ul');

for (let clave in estudiante) {
    let elementoLista = document.createElement('li');
    elementoLista.textContent = estudiante
}

console.log(lista)
   