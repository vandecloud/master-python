"""
SET
es un tipo de dato, para tener una coleccion de valores,
pero no tiene un indice ni orden.
"""

personas = {
    "Pablo",
    "Carlos",
    "Roberto"
}

print(personas)
personas.add("Armando")
personas.remove("Carlos")
print (personas)
print(type(personas))