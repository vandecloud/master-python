"""
Pedir dos numeros al usuario y hacer todas las operaciones basicas
de una calculadora y mostrarlo por pantalla.

"""


valor1 = int(input(f"Introducir primer valor a calcular "))
valor2 = int(input(f"Introducir segundo valor a calcular "))


multi = valor1 * valor2
div = valor1 / valor2
rest = valor1 - valor2
sumar = valor1 + valor2
print("\n####CALCULADORA####")
print (f"El resultado de Mutiplicar {multi}")
print (f"El resultado de Dividir {div}")
print (f"El resultado de Restar {rest}")
print (f"El resultado de Sumar {sumar}")