frase="Aprendiendo a programar en Python"
print(frase[0]) #Se printea la letra 1
print(frase[1])
print(frase[-1]) #Da la ultima letra del string, es decir, la n
print(frase[-2])

mi_substring1=frase[:5] #Da las 5 primeras letras del string, es decir, apren
print(mi_substring1)
mi_substring2=frase[4:] #Da todo el string menos las 4 primeras letras del string
print(mi_substring2)

print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase.count("pr")) #2
print(frase.count("pr", 0, 6)) #1
print(frase.find("pr")) #Posicion de la primera vez que aparece
print("pr" in frase)
print("calc" in frase)
frase=frase.replace("Python", "python3", 1)
print(frase)
print(frase.isnumeric()) #Para saber si es numerica la variable frase
