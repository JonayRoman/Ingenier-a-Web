#Dada la siguiente lista [12, 23, 5, 29, 92, 64] realiza las siguientes operaciones y vete mostrando la lista 
# resultante por pantalla:
###1.Elimina el último número y añádelo al principio.
###2.Mueve el segundo elemento a la última posición.
###3.Añade el número 14 al comienzo de la lista.
###4.Suma todos los números de la lista y añade el resultado al final de la lista.
###5.Fusiona la lista actual con la siguiente: [4, 11, 32]
###6.Elimina todos los números impares de la lista.
###7.Ordena los números de la lista de forma ascendente.
###8.Vacía la lista.

lista = [12, 23, 5, 29, 92, 64]
lista.insert(0,lista.pop())
print(f"1. {lista}")
lista.insert(5,lista.pop(1))
print(f"2. {lista}")
lista.insert(0,14)
print(f"3. {lista}")
suma = sum(lista)
lista.append(suma)
print(f"4. {lista}")
lista_2 = [4, 11, 32]
lista.extend(lista_2)
print(f"5. {lista}")
lista = [num for num in lista if num % 2 == 0]
print(f"6. {lista}")
lista.sort()   
print(f"7. {lista}")
lista.clear()
print(f"8. {lista}")