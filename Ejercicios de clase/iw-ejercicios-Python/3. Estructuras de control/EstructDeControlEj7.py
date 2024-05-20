#Mejora el programa anterior, de forma que el usuario pueda introducir tantos números como quiera. El programa solicitará números 
# al usuario hasta que introduzca la palabra "fin". Entonces mostrará el mayor de todos por pantalla.

num1 = int(input("Introduce el primer numero:"))
num2 = ""
while num2 != "fin":
    num2 = input("Introduce el siguiente numero o escribe fin:")
    if num2 != "fin":
        if int(num1) <= int(num2):
            num1 = num2
print(num1)