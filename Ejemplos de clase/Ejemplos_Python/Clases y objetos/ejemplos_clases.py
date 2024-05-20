class Persona: #Los atributos por defecto son publicos
    nombre = "Josune"
    edad =24
    def camina(self):
        print(self.nombre + " esta caminando")
        
p1 = Persona()
p1.camina()
print(p1.nombre)

#Constructor __init__ (Solo puede existir uno)
class persona:
    #Atributos de clase o estatico
    contador = 0
    def __init__ (self, nombre, apellido, edad): #self hay que pasarlo si se quiere
        #Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        Persona.contador += 1
    def camina(self):
        print(self.nombre + " esta caminando")
        
p2 = Persona("Josean", "Hernandez", 40)
p2.camina()
print(p2.contador)
p3 = Persona("Alex", "Fernandez", 10)
print(Persona.contador)

#Protected y Private
class Persona:
    def __init__ (self, nombre, apellido, edad): #self hay que pasarlo
        #atributo de instancia
        self.__nombre = nombre #privado
        self._apellido = apellido #protegido
        self._edad = edad #protegido
        
    def camina(self):
        print(self.nombre + " esta caminado")
        
p4 = Persona("Aiur", "Gonzalez", 12)
print(p4._apellido)
print(p4.__nombre)