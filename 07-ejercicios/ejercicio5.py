""""
Hacer un programa que muestre todos los numeros entre dos numeros
que diga el usuario
"""

rango_inicio = int(input("Introducir primer numero del rango: "))
rango_final = int(input("Introducir el segundo numero del rango: "))

if rango_inicio < rango_final:
    for contador in range(rango_inicio, (rango_final + 1)):
      print(f"Estos son los numero en el rango seleccionado")
      print(contador)
else:
    print("El rango inicial es menor que el rango final")