#Escribe un programa que solicite dos números enteros al usuario y muestre por pantalla la suma de todos los 
# números enteros que hay entre los dos números (ambos números incluidos).

num_1 = int(input("Introduce el primer numero: "))
num_2 = int(input("Introduce el segundo numero: "))

for i in range(num_1, num_2 + 1):
    total = 0
    total = total + i