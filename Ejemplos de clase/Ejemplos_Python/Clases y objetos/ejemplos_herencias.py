class Persona:
    def __init__ (self, nombre, apellido, edad): #self hay que pasarlo
        #atributo de instancia
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 
        
    def camina(self):
        print(self.nombre + " esta caminado")
        
class Estudiante(Persona): #Existe la multiherencia y separado por coma
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.nota_media = 0
        self.repetidor = False
    def es_repetidor(self):
        print(self.repetidor)
        
p2 = Estudiante("Josean", "Hernandez", 40)
p2.es_repetidor()
p2.camina()