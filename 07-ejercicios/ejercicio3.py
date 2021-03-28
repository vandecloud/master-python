"""
Escribir un programa que muestre los cuadrados 


(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. resolverlo con or y con while

"""

# WHILE
contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print (f"El cuadrado de {contador} es {cuadrado}")

    contador += 1

contador2 = 1

# FOR
for contador2 in range (61):
    cuadrado2 = contador2 * contador2
    print (f"El cuadrado de {contador2} es {cuadrado2}")

    
    contador2 += 1 
