/* 
○ Genera una tabla HTML como la de la imagen. Los datos de la tabla deberán estar almacenados en un array de 
objetos con la siguiente estructura:
○ Del punto anterior Añádele un formulario para recoger los valores de una nueva 
tarea y que la añada al final de la tabla al clickar en el botón de envío.
○ Mejora la aplicación añadiendo un enlace o botón de borrado a cada una de las tareas.
○ Sigue mejorando la aplicación y añade la posibilidad de marcarla como resuelta (es suficiente con añadir un 
botón y que el texto se muestra tachado cuando esté resuelta. */

let tareas = [
    {
        id: 1,
        fecha: "03-10-2020",
        responsable: "Mikel",
        descripcion: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {
        id: 2,
        fecha: "12-08-2020",
        responsable: "Unai",
        descripcion: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {
        id: 3,
        fecha: "11-12-2020",
        responsable: "Ane",
        descripcion: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {
        id: 4,
        fecha: "07-06-2020",
        responsable: "Nora",
        descripcion: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
];

function crearTablaCompleta (listadoTareas) {
    let tabla = 
        `<table id="tabla">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Fecha</th>
                    <th>Responsable</th>
                    <th>Descripción</th>
                </tr>
            </thead>
            <tbody>      
                <tr>
                    
                </tr>
            </tbody>`
    for (let tarea of listadoTareas) {
        tabla += crearTabla(tarea.id, tarea.fecha, tarea.responsable, tarea.descripcion)
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTabla (id, fecha, responsable, descripcion) {
    return `
        <tr>
            <td>${id}</td>
            <td>${fecha}</td>
            <td>${responsable}</td>
            <td>${descripcion}</td>
        </tr>`;
}

let tabla = crearTablaCompleta(tareas); 
document.getElementById('tareas').innerHTML = tabla;