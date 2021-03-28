"""
Escribir un programa que añada valores a una lista mistras que su 
logitud sea menor a 120 y luego mostrar la lista

- usar While y for

"""
coleccion = []

for contador in range(0, 2):
    coleccion.append(f"Elemeneto-{contador}")
    print("Mostrando el:" + coleccion[contador])


print (len(coleccion))


coleccion2 = []
x=0  #Contador
while x < 120:
    coleccion2.append(f"elemento- {x}")
    print("Mostrardo el:" + coleccion2[x])
    x += 1
print (len(coleccion))


print("==============================================")
coleccion = []

for contador in range(0, 2):
    coleccion.append(f"Elemeneto-{contador}")
    print("Mostrando el:" + coleccion[contador])


print (len(coleccion))


coleccion2 = []