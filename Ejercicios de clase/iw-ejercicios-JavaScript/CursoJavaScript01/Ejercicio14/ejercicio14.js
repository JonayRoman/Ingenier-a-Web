/* Sigue las siguientes instrucciones:
● Crea un objeto llamado aplicacion con la propiedad nombre (el valor será “Web App Industrial”).
● Añade las propiedades llamadas puerto (con el valor 8000) y hostname (con el valor “localhost”)
● Muestra el valor de cada propiedad por pantalla.
● Elimina la propiedad hostname. */

//1
let aplicacion = {
    nombre: "Web App Industrial"
};
//2
aplicacion.puerto = 8000;
aplicacion.hostname = "localhost";
//3
console.log(aplicacion.nombre);
console.log(aplicacion.puerto);
console.log(aplicacion.hostname);
//4
delete aplicacion.hostname;
console.log(aplicacion);