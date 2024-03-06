#Escribe un programa que solicite al usuario una frase. A continuación le solicitará la letra que 
#quiere reemplazar y por qué letra deberá reemplazarse. Por último el programa mostrará el 
#número de veces que la letra está presente en la frase y el resultado final tras reemplazarla.
frase = input("Escribe una fase: ")
letra_vieja = input("¿Que letra quieres reemplazar? ")
letra_nueva = input("¿Por que letra la quieres reemplazar? ")

while len(letra_vieja) != 1 or len(letra_nueva) != 1:
    print("Escribe una sola letra")
    letra_vieja = input("¿Qué letra quieres reemplazar? ")
    letra_nueva = input("¿Por qué letra la quieres reemplazar? ")

num_letras = frase.count(letra_vieja)
frase_nueva = frase.replace(letra_vieja, letra_nueva)

print(str(num_letras) + " apariciones.") 
print(frase_nueva)
