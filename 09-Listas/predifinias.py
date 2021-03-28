cantantes = ["miranda", "Julio Iglesias", "Sin Bandera"]
numeros = [1, 2, 5, 4, 8, 9]

#Ordenar la lsta

numeros.sort()
print(numeros)

#Agregar elementos

cantantes.append("Rodrigo")
cantantes.insert(4, "Talia") # Debemos indicar en que inidice seca a colocar el elemento (4)
print(cantantes)

# Eliminar elementos

cantantes.pop(1) #Remover por indice
cantantes.remove("Talia")# Remover por nombre de elemento

print(cantantes)

# Dar la vuelta a la lista (orden inverso)

print(numeros)
numeros.reverse
print(numeros)
#Contar los elementos de una lista
print(len(numeros))

#Buscar dentro de una lista
print("miranda" in cantantes)

# Cuantas veces aparece un elemento
numeros.append (8) #Agregamos un elemento a la lista 
print(numeros.count(8))

# obterner el indice

print(cantantes.index("miranda")) # ubicacion del elemento en el indice

#Unir listas
cantantes.extend(numeros)
print(cantantes)
