# Programacion orientada a objetos (POO o OOP)

# definir una clase ( Model para crear mas objetos de ese tipo)
# (coche) con caracteristicas similares

class coche:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje= 500
    plazas = 2

    #Metodos, son acciones que hace el objeto (coche) (funciones)

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1
    
    def getVelocidad (self):
        return self.velocidad

    
# fin definicion clase

#Crear un objeto / instanciar la clase

#coche = coche()

#print(coche.marca, coche.color)
print ( "Velocidad actual", coche.velocidad )

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print ( "Velocidad nueva al acelerar", coche.velocidad )


coche.frenar()
coche.frenar()

print ( "Velocidad al frenar actual", coche.velocidad )


# Metodo get / set

print("###########Coche 1 ##############")
class coche:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje= 500
    plazas = 2

    #Metodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self,color):
        self.color = color

    def getColor (self):
        return self.color

    def setModelo (self,modelo):
        self.modelo = modelo        

    def getModelo (self):
        return self.modelo

    def setCaballaje (self,caballaje):
        self.caballaje = caballaje
    
    def getCaballaje(self):
        return self.caballaje

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -=1
    
    def setVelocidad(self,velocidad):
        self.velocidad = velocidad

    def getVelocidad (self):
        return self.velocidad

coche1 = coche()

coche1.setColor("Amarillo")
coche1.setModelo ("Morcielago")
coche1.setVelocidad (6000)

print(coche1.marca, coche1.getColor())

print(f"Velocidad actual", coche1.getVelocidad())

# Multiples objetos
print("###########Coche 2 ##############")

coche2 = coche()

coche2.setColor("Bordo")
coche2.setModelo ("VW")
coche2.setVelocidad (400)

print(coche2.marca, coche2.getColor())
print(f"Velocidad actual", coche2.getVelocidad())


# Prin.type nos trae el tipo de objeto que en este caso seria derivado de una clase
#class '__main__.coche'

print(type(coche2))

#Clases molde para crear objetos
    #Aributos de las clases
    #Metodos (funciones), las acciones que puede hacer las clases

#Abtraccion 
#Herencia de clases mas genericas a clases mas especificas
#Modularidad 
#Ocultacion /encapsulacion los datos solo deben modificarse desde dentro de cada clase


