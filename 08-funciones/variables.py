"""
Variables Locales: Se definen dentro de la funcion y no se puede
usar fuera de lla, solo esta disponible dentro.
a no ser que hagamos un return

Variables Globales: Son las que se declaran fuera de la funcion
y estan disponibles dentro y fuera de ellas

"""

# variables globales

frase = "Solo se que no se nada"
print (frase)

def holaMundo():
    frase = "Hola Mundo!!"
    print (frase)
    year = 2021
    print(year)

    global website
    website = "www.google.com.ar"
    print(f"Dentro:", website)
    return "Dato devuelto: " + str(year)


print(holaMundo())
print("FUERA:", website)