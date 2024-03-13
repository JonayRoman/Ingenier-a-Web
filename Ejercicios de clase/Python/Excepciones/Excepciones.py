try:
    divisor = int(input("Introduce un divisor: "))
    dividiendo = 150
    resultado = dividiendo / divisor
    print(resultado)
except ValueError:
    print("Numero no valido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally: #El finally no es obligatorio. Si esta se ejecuta siempre despues de la ejecucion
    print("Ejecutar finally antes de salir")