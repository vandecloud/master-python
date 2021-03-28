"""
hacer un programa que pida numero al usuario
indefinidamente hasta meter el numero 111

"""

contador = 1
while contador < 5:
    numero = int(input("Introducir un numero: "))
    if numero == 111:
        break
    else:
       print("continua introduciendo valores")