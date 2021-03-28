"""
LISTAS (arrays)
son colecciones o conjutos de datos/valores, bajo un unico 
nombre.
para acceder a esos valores odemos usar un indice numerico.

"""
"""
# Definir lista
pelicual = "Batman"
peliculas = ["Batman", "Spidemar", "superman" ]
cantantes = list(("miranda", "ricardo arjona", "shakira", "chayanne"))
años = list(range(2020, 2050))
variada = ["victor", "30", 40, True, "texto"]

print(peliculas)
print(cantantes)
print(años)
print(variada)

# Indices
#Puedo modificar mi lista
peliculas[1] = "Gran Torino"
print(peliculas)

#Comienza la lista del 0 en adelante
print(peliculas [1])
#Comienza la lista del ultimo al primero
print(peliculas[-2]) 
# Rango de elementos
print(cantantes [1 : 3])
# Saca todos los elementos a partir de 1 o del indice que indiquemos
print(peliculas[1:])


# Añadir elemento a lista

cantantes.append ("Talia")
cantantes.append("Rodrigo")
print(cantantes)

#Recorrer lista

print ("\n*************LISTAR NUEVAS PELICULAS*************")

nueva_pelicula =""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introducir la nueva pelicula:" )
    if nueva_pelicula != "parar": # para evitar el append del condicional While
     peliculas.append(nueva_pelicula)

print ("\n*************LISTADO DE PELICULAS*************")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""
# Listas Multidimensionales

print("\n***************Listado de contactos********************")

contactos =[ 
    [
        "Anotinio",
        "antonio@antonio.com"
    ],

    [
        "Pablo",
        "pablo@pablo.com"

    ],
    [
        "Pedro",
        "pedro@pedro.com"
    ]

]
"""
print(contactos)
#Si quiero sacar un elemento dentro de mi lista
print(contactos [1][1])
"""
# Recorrer todos los contactos

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) ==0:
            print("Nombre:" + elemento)
        else:
            print("Email:" + elemento)

    print("\n")

