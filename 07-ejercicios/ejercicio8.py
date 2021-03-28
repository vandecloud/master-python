"""
Calcular el % de un numero dado
cuanto es el X % de y 

"""

numero = int(input("Intruducir el numero:  "))
porcentaje = int(input("Introducir el % a calcular: "))


resultado = (porcentaje * numero) / 100
print (f" El % calculado es:", str(resultado))