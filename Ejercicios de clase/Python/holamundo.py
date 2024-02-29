print("Hello world")
#Dinámicamente tipado
edad=25
print("La variable 'edad' es de tipo: " + str(type(edad))) #No hace falta poner el type, con poner str vale.
print(str(edad))
print(edad) #Se puede mostrar asi, pero en caso de querer concatenarlo, pasarlo a str.
edad="Tengo 25 años"
print("La variable 'edad' es de tipo: " + str(type(edad)))
print(edad)
#Indentación
x=5
if x==5:
    print("El valor de x es " + str(x)) #Como no se pueden concatenar int, se convierte a str.
