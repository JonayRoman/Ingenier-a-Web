#res ambito local, dentro de la funcion, y cuando se termina la ejecucion se destruye
def suma(a,b):
    res = a + b
    print(res)
#print(res) #error
suma(1,4)

#ambito global
a = 5
def multiplicar_por_dos():
    print(a*2) #no se modifica la variable de ambito global, solo se lee y se usa
multiplicar_por_dos()

#x = 10
#def mostrarX():
#    x = x + 2 #error, podemos acceder pero no modificar
#    print("El valor de X es " + x)
#mostrarX()

x = 10
def mostrarX():
    global x
    x = x + 2 #para que no de error
    print("El valor de X es ", x)
mostrarX()