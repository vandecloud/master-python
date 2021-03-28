"""
hacer un programa todos los numeros impares entre dos numeros que decida el usuario

"""

numero1 = int (input("Introducir el primer valor: "))
numero2 = int (input("Introducir el segundo valor: "))

print(f"Valores IMPARES")
if numero1 < numero2:
    for valor in range(numero1, (numero2 +1)):
        if not (valor) %2 == 0:
            print (valor)
else:
    print(f"El rango es incorrecto numero 1 debe ser menor a numero 2")