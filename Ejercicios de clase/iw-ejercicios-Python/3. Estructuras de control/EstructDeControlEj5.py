#Mejora el programa anterior para que solo permita 3 intentos. Cada vez vez que el usuario introduzca datos 
# de acceso incorrectos el programa mostrará el mensaje: "Datos incorrectos. Le quedan X intentos.", 
# siendo X el número de intentos restantes. Tras el tercer fallo el programa mostrará el mensaje "Has agotado 
# todos tus intentos." y finalizará.

contador = 3
while contador != 0:
    usuario = input("Introduce el nombre de usuario: ")
    clave = input("Introduce la contraseña: ")

    if usuario != "root" or clave != "root":
        contador = contador - 1
        if contador != 0:
            print(f"Datos incorrectos. Le quedan {contador} intentos")
    else:
        print("¡Bienvenido!")
        break
else:
    print("Has agotado todos tus intentos.")
