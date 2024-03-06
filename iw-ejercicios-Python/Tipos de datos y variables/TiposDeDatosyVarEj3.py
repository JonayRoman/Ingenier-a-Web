#Escribe un programa que genere un string compuesto por los primeros 3 caracteres y los últimos 
#3 caracteres de un string introducido por el usuario. Pista: puedes utilizar la función len() en la 
#obtención de los últimos 3 caracteres.

frase = "aprendiendo a programar en python"
string_1 = frase[0:3]
string_2 = frase[-3:]
print(string_1 + string_2)
