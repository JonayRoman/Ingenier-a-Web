#Crea un programa que reciba 5 números del usuario y muestre el mayor de todos por pantalla.

i = 4
num1 = int(input("Introduce el primer numero:"))
while i != 0:
    i = i - 1
    num2 = int(input("Introduce el siguiente numero:")) 
    if num1 <= num2:
        num1 = num2
print(num1)

         