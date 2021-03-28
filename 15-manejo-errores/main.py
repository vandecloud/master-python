"""
Capturar excepciones y manejo de errores en codigo
susceptible a fallos/errores

"""


try:
        nombre = input ("¿cual es tu nombre?:  ")
        if len(nombre) > 1:
                nombre_usuario = "Nombre es" + nombre
                print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
fin