#Crea un programa que solicite al usuario el radio de un círculo y calcule el área. Nota: 
# Utiliza 3.14159 como número PI para el cálculo del área.

radio = float(input("Introduce el radio del circulo: "))
pi = 3.14159
area = pi * radio**2
print("El area del circulo es: " + str(area))