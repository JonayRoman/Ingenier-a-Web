/* Crea dos arrays, uno con 4 tipos de animales y otro con 3 nombres de colores.
■ Muestra por pantalla el segundo elemento de cada array.
■ Obtén el número de elementos de cada array y muéstralo por pantalla.
■ Añade un elemento al final del array animales utilizando una función.
■ Añade un elemento al principio del array colores utilizando una función.
■ Recorre el array animales mostrando por pantalla cada uno de sus elementos. */
let animales = ["tigre", "leon", "lobo", "zorro"];
let colores = ["rojo", "azul", "verde"];
//1
console.log(animales[1]);
console.log(colores[1]);
//2
console.log("Número de animales: " + animales.length);
console.log("Número de colores: " + colores.length);
//3
animales.push("ardilla")
console.log(animales);
//4
colores.unshift("amarillo");
console.log(colores);
//5
for(let i = 0; i < animales.length; i++) {
    console.log(animales[i]);
}
