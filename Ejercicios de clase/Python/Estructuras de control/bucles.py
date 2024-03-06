#while
contador = 0
while(contador < 5):
    contador+=1
    print("Interacion numero",contador)
print("fin")

contador = 0
while contador < 5:
    contador+=1
    print("Interacion numero {}".format(contador))
    if contador == 3:
        break
print("fin")

#for (FOREACH)
alumnos = {"Gaizka", "Mikel", "Jon", "Ruben"}
for alumno in alumnos:
    print(alumno)
    
#Recorrer un string
alumno = "Gaizka"
for letra in alumno:
    print(letra)

numeros = [5, 46, 3, 5, 2, 5, 55, 9]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
    
#For con else - si termina el for completo
alumnos = {"Gaizka", "Mikel", "Jon", "Ruben"}
for alumno in alumnos:
    print(alumno)
else:
    print("No quedan mas alumnos")
    
#Funcion range() - para hacer un bucle iterativo
for i in range(3): #imprime del 0 al 2
    print(i)

for i in range(1,10,2):
    print(i) #del 1 al 10 de dos en dos

alumnos = {"Gaizka", "Mikel", "Jon", "Ruben"}
for i in range(len(alumnos)):
    print(alumnos[i]) #da los alumnos de la posicion 0 a la posicion 3
    