#Crea un programa que solicite al usuario 5 números y los guarde en una lista. A continuación el programa 
# pedirá otros 5 números al usuario almacenándolos en una segunda lista. El programa mostrará al usuario una 
# lista que contenga los números que tienen en común las dos listas anteriores.

numeros_1 = []
numeros_2 = []
i = 10
while i != 0:
    i -= 1
    while len(numeros_1) != 5:
        num = int(input("Introduce un numero para la primera lista: "))
        numeros_1.append(num)
    while len(numeros_2) != 5:
        num = int(input("Introduce un numero la segunda lista: "))
        numeros_2.append(num)
print(f"Lista 1: {numeros_1}")
print(f"Lista 2: {numeros_2}")
numeros_1_sinRepetir = set(numeros_1)
numeros_2_sinRepetir = set(numeros_2)
print(f"Lista 1 sin repetir numeros: {numeros_1_sinRepetir}")
print(f"Lista 2 sin repetir numeros: {numeros_2_sinRepetir}")
num_repetidos = numeros_1_sinRepetir.intersection(numeros_2_sinRepetir)
lista_numeros_repetidos = [num_repetidos]
print(f"Lista de los numeros repetidos: {lista_numeros_repetidos}")