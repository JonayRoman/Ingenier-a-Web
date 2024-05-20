/* Captura los eventos de click en los enlaces, detén la navegación y muestra un alert con la
dirección de la URL */

<a href="/" onclick="event.preventDefault()">Click</a>


var pararEvento = function(event) {
    let enlace = document.getElementsByTagName('a');
    alert(enlace);
    event.preventDefault();
   };
   
