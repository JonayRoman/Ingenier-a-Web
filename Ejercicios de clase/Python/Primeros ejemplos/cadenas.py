mi_nombre="Jonay"
print(mi_nombre)
mi_nombre="I'm Jonay"
print(mi_nombre)
frase="""Esto es una frase
muuuuuuy laaaarga"""
print(frase)

#Concatenacion
palabra1="Hola"
palabra2="mundo"
frase=palabra1 + " " + palabra2
print(frase)

frase=" ".join([palabra1,palabra2])
print(frase)

frase="Meses: {}, {} y {}".format("Enero", "Febrero", "Marzo")
print(frase)
frase="Meses: {1}, {0} y {2}".format("Enero", "Febrero", "Marzo")
print(frase)
frase="Meses: {ene}, {feb} y {mar}".format(ene="Enero", feb="Febrero", mar="Marzo")
print(frase)

#f-string
nombre="Jonay"
edad=40
saludo=f"Me llamo {nombre} y tengo {edad} años"
print(saludo)

valor1=2
valor2=4
print(f"El resultado de multiplicar {valor1} y {valor2} es igual a {valor1 * valor2}")

#conversiones
edad=20