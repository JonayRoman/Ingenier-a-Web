#Crea un programa que solicite un número al usuario y devuelva el siguiente mensaje:
###Si es mayor que 0: "Es un número positivo."
###Si es igual a 0: "Es igual a cero.
###Si es menor que 0: "Es un número negativo."

num = int(input("Introduce un numero: "))
if num > 0:
    print("El numero es positivo")
elif num == 0:
    print("El numero es igual a 0")
else:
    print("El numero es negativo")