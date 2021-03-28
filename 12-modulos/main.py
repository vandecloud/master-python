"""
Modulos: Son funcionalidades ya hechas para reutilizar
en python hay muchos modulos que se pueden consultar 

podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros propios
Modulos
"""
"""
import mimodulo #Importa todas las funciones que esten declaradas en mi archivo modulo
from mimodulo import holaMundo #Importa solo la funcion que me interesa que esta dentro de mi archivo modulo
from  mimodulo import * #Importar todos los modulos y luego invoco las funciones

#print(mimodulo.calculadora(8,5,basicas=True))
#print(mimodulo.holaMundo("Hola Pablo"))

print(holaMundo("Pablo"))
print(calculadora(4,5, basicas=True))
"""
#Modulos fechas
import datetime

print (datetime.date.today())
fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada =fecha_completa.strftime ("%d/%m/%Y, %H:%M:%S")
print(f"fecha_personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

#Modulo Matematicas

import math

print("Raiz cuadrada de 10", math.sqrt (10))
print("Numero pi:", float(math.pi))
print("Redondear:", (math.ceil (math.pi)) )#Redondea a la Alta
print("Redondear:", (math.floor (math.pi)) )#Redondea a la Baja

#Modulo Random

import random

print ("Numeros aleatorios entre 15 y 555:", random.randint(15,555) )

