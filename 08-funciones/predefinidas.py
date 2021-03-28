nombre = "Pablo Vandecaveye"

#funciones generales

print(nombre)

print(type(nombre))

# Detectar el tipado

comprobar = isinstance (nombre, int)
if comprobar:
    print("esa variable es un entero")
else:
    print("esa variable no es un entero")

# limpiar espacios

frases = "     Mi contenido  "
print(frases)
print(frases.strip())

# Elimibar varibles
year = 2021
print(year)
del year

# Comprobar variables vacias

texto = "  ff  "

if len(texto) <= 0:
    print(" La variable esta vacia ")
else:
    print("La variable tiene contendido ", len (texto))

# Encontar caracteres
frase = "La vida es bella"
print(frase.find("vida"))



# Remplazar palabras en un string

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())