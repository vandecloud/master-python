"""
DICCIONARIOS

Un diccionario es un tipo de dato que almacena un conunto de datos.
en formato clave > valor
es parcecido a un array asociativo o un objeto json.

"""
"""
persona = {

    "nombre": "Pablo",
    "apellido": "Vande",
    "Web": "a definir"
}

print(type(persona))

print(persona["apellido"])  # Acceder al indice que indicamos
"""
contactos = [
    {"nombre": "pablo",
     "email": "pablo@pablo.com"
     },
    {
        "nombre": "roberto",
        "email": "roberto@roberto.com"
    },
    {
        "nombre": "camilo",
        "email":    "camilo@camilo.com"
    }
]

#print(contactos)

#print(contactos[1]["email"])

print ("n\Listado de contacos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto ['nombre']}")
    print(f"email del contacto: {contacto ['email']}")
    print(f"**************************************")