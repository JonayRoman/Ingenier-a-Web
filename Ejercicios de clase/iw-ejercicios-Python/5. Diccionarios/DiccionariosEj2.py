#Recorre un diccionario y crea una lista solo con los valores que contiene, sin añadir valores duplicados.

lista_edades = []
lista_sin_duplicados = []
usuarios = {
    "Mikel": {
        "nombre": "Mikel",
        "edad:": "3"
    },
    "Ane": {
        "nombre": "Ane",
        "edad:": "8"
    },
    "Amaia": {
        "nombre": "Amaia",
        "edad:": "12"
    },
    "Unai": {
        "nombre": "Unai",
        "edad:": "5"
    },
    "Jon": {
        "nombre": "Jon",
        "edad:": "8"
    },
    "Ainhoa": {
        "nombre": "Ainhoa",
        "edad:": "7"
    }
}

for usuario in usuarios.values():
    lista_edades.append(int(usuario["edad:"]))
for elemento in lista_edades:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(lista_sin_duplicados)
    