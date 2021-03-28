"""
Escribir un script que nos muestre por pantalla todos los numeros pares
del 1 al 120
"""

"""
numero = 1 

while numero <= 120:
    if numero %2 == 0:
        print(f"El ciclo va por {numero}" )
        numero += 1
"""
numero = 1

for numero in range (1, 121):
    if numero %2 == 0:
        print(f"{numero} es PAR")
    else:
     print(f"{numero} es IMPAR")