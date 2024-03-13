#Escribe un programa que contenga las siguientes variables:
#nombre: tipo string y valor "Michael Jordan"
#edad: tipo integer y valor 50
#media_puntos: tipo float y valor 28.5
#activo: False
#El programa deberá mostrar en pantalla todos los valores.

nombre="Michael Jordan"
edad=50
media_puntos=28.5
activo=False

print(nombre)
print(edad)
print(media_puntos)
print(activo)
print(nombre + " tiene " + str(edad) + " años y ha metido una media de " + str(media_puntos) + " puntos.")
print(f"{nombre} tiene {edad} años y ha metido una media de {media_puntos} puntos.")