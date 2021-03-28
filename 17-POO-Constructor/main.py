from coche import Coches

carro = Coches("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coches("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coches("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coches("Rojo", "Mercedes", "Clase A", 350, 400, 4)


print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar el tipado

if type (carro3) == Coches: #Comparar con la clase 
    print ("Es un objeto correcto")
else:
    print("No es un objeto")

# Visibilidad

print(carro.soy_publico)
#print(carro.__soy_privado)
print (carro.getPrivado())