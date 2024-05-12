/* Modifica el código del ejemplo anterior para que muestre el valor de todas las propiedades del objeto 
aplicacion mediante un bucle for */

let aplicacion = {
    nombre: "Web App Industrial"
};
aplicacion.puerto = 8000;
aplicacion.hostname = "localhost";
for (elemento in aplicacion) {
    console.log(elemento + ": " + aplicacion[elemento]);
}