#Escribe un programa que solicite al usuario dos números y una frase. El primer número 
#introducido se corresponderá a la posición de inicio del substring que deberá mostrar el 
#programa por pantalla. El segundo número indicará la longitud de dicho substring.

num_1 = int(input("Escribe un número: "))
num_2 = int(input("Escribe otro número: "))
frase = input("Escribe una frase con una longitud superior a 10 caracteres: ")

if len(frase) < 10:
    print("La frase debe tener más de 10 caracteres")
else:
    string = frase [num_1:num_1 + num_2]
    print(string)
   
    