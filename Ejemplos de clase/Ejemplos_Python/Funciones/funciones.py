#Funciones
def saludo(nombre):
    print(f"Hola {nombre}. ¡Bienvenido!")

saludo("Jonay")

def saludo(nombre = "Antonio"):
    print(f"Hola, {nombre}. ¡Bienvenido!")
    
saludo("Jonay")
saludo()

#Parametros posicionales vs parametro con palabras clave (keyword arguments)

def suma(a,b):
    res = a + b
    print(res)
    
#Se puede hacer de estas dos maneras
suma(1,4)
suma(a=1,b=6)

def suma(a,b):
    res = a + b
    return res
print(suma(2,3))

def suma(*args):#pasas una lista de valores o una tupla
    res = 0
    for value in args:
        res += value
    print(res)
suma(1,6,34,12,5)

def suma(**kwargs): #pasas un diccionario (tiene clave)
    res = 0
    for value in kwargs.values():
        res += value
    print(res)
suma(a=5,b=98,c=23,d=2)
#args y kwargs se puede llamar como queramos (el asterisco y doble asterisco obligatorios) lo normal
#es encontrarlos con esos nombres