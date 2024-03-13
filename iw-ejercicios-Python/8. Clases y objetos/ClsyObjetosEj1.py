#Crea la clase Coche que contenga las siguientes propiedades:
###matrícula (string)
###marca (string)
###kilometros_recorridos (float)
###gasolina (float)
#La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir y 
# sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. El método también restará al 
# valor de gasolina el resultado de los kilómetros multiplicado por 0'1. La clase también contendrá otro método 
# llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable 
# gasolina. Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la 
# gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario repostar para recorrer la cantidad 
# indicada de kilómetros".