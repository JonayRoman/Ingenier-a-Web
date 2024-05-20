#Escribe un programa que solicite el nombre, DNI y edad, lo almacene en 3 variables distintas y 
#muestre por pantalla los valores introducidos.

nombre = input("¿Cual es tu nombre?")
dni = input("¿Cual es tu DNI?")
edad = input("¿Cuantos años tienes?")
print(f"Mi nombre es {nombre}, mi DNI es {dni} y tengo {edad} años.") #Forma print f
print("Mi nombre es " + nombre + ", mi DNI es " + dni + " y tengo " + edad + " años.") #Forma print concatenado

