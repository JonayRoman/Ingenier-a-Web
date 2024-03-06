#Crea un programa que solicite al usuario un número del 1 al 10 y muestre por pantalla la tabla de 
# multiplicación del 1 al 10.

num = int(input("Introduce un numero: "))
for i in range(11): 
    resultado = num * i 
    print(resultado)