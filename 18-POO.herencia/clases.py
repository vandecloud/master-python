# Herencias : es la posibilida de compartir atributos y metodos
# entre clases. y que diferentes clases hereden de otras


class Persona:
    """
    # Denimos mi modelo persona con atributos bases que hacen a 
    cualquier clase persona.
    
    Nombre
    apellidos
    altura 
    edad 
    """
    # Caracteristicas 
    # Definir el metodo 
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    # definir set
    
    def setNombre (self, nombre):
        self.nombre = nombre
        
    def setApellido (self, apellidos):
        self.apellidos = apellidos
    
    def setAltura (self, altura):
        self.altura = altura
                
    def setEdad (self, edad):
        self.edad = edad
        
        # Una persos puede hacer muchas acciones 
    
    def hablar(self):
        return "Estoy Hablando"
    
    def caminar (self):
        return "Estoy caminando"
    
    def dormir (self):
        return "Estoy Durmiendo"
    
    # Otras acciones que pueden hacer las persoanas 
    
class Informatico(Persona): # Definimos una nueva clase que tiene como herencia la clase persona
    """
    lenguajes
    Experiencia
        
    """
    #Definimos un metodo contructor
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    # Acciones del programador
    
    def programar(sefl):
        return "Estoy programando"
    
    def repararPC (self):
        return "eh reparado tu pc"
    
    
class TecnicoRedes(Informatico):
#Acceder al contructor de las clases padres


    def __init__(self):
        super().__init__() #Acceder al contructor de las clases padres
        self.auditarRedes = "experto"
        self.experienciaRedes = 15
    def auditoria (self):
        return "Estoy auditando una red"