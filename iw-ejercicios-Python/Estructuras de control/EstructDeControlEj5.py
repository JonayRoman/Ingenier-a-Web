#Mejora el programa anterior para que solo permita 3 intentos. Cada vez vez que el usuario introduzca datos 
# de acceso incorrectos el programa mostrará el mensaje: "Datos incorrectos. Le quedan X intentos.", 
# siendo X el número de intentos restantes. Tras el tercer fallo el programa mostrará el mensaje "Has agotado 
# todos tus intentos." y finalizará.

usuario = input("Introduce el nombre de usuario: ")
clave = input("Introduce la contraseña: ")

if usuario == "root" and clave == "root":
    print("¡Bienvenido!")
else:
    print("Acceso fallido")