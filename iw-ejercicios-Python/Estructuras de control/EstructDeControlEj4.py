#Escribe un programa que solicite al usuario un nombre de usuario y contraseña. El programa mostrará el 
# mensaje "¡Bienvenido!" si el usuario introduce los siguientes datos:
###Nombre de usuario: root
###Contraseña: toor
###Si los datos de acceso son incorrectos mostrará el mensaje "Acceso fallido" y el programa finalizará.

usuario = input("Introduce el nombre de usuario: ")
clave = input("Introduce la contraseña: ")

if usuario == "root" and clave == "root":
    print("¡Bienvenido!")
else:
    print("Acceso fallido")