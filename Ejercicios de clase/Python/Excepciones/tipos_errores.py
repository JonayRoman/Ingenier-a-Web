#typeError: unsupported operend tyoe(s) for +: "int" and "str"
#print(1 + "1")

#ValueError: invalid literal for int() with base 10: "Hola"
#print(int("Hola"))

#NameError: name 'estudiante' is not defined
#print(estudiante)

#IndexError: list index out of range
lista = [1,6,7]
#print(lista[5])

#keyError: 'aprobados'
estudiante = {
    "nombre": "Iñaki Perurena",
    "edad": 30,
    "nota_media": 7.25,
    "repetidor": False
}
print(estudiante["aprobados"])