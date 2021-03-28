"""
Funciones:
una funcion es un conjuto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocanto a la funcion tantas
veces como sea necesario.

def nombreDeMiFuncion(parametros):
    #Bloque de codigo / conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)
pudeo invocarla tantas veces lo necesite
nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1

print("#### Ejemplo 1 ####")

# definir funcion

def muestraNombre():
    print("Pablo")
    print("Dai")
    print("valentin")
    print("Matias")
    print("Irma")
    print("Liliana")
    print("\n")

# invocar funcion

muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2 parametros

print("#### Ejemplo 2 ####")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")
    if edad > 18:
        print ("Eres mayor de Edad")
    else:
        print("Eres menor de edad")
nombre = input("Introduce tu nombre:")
edad = int(input("Introduce tu edad:"))
mostrarTuNombre(nombre, edad)


# Ejemplo 3 parametros

print("#### Ejemplo 3 ####")


def tabla(numero):
    print(f"La tabla de multiplicar del numero:  {numero}")
    

    for contador in range (11):
        operacion = numero * contador
        print (f"{numero} x {contador} = {operacion}")

    print ("\n")

# Ejemplo 3.1
print("--------------------")

for numero_tabla in range (1, 11):
    tabla(numero_tabla)

# Ejemplo 4 parametros opcionales

print("#### Ejemplo 4 ####")

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Pablo Vandecaveye", 123344)

# Ejemplo 5 parametros opcionales y return o devolver datos


print("#### Ejemplo 5 ####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("pablo"))


# Ejemplo 6 parametros opcionales y return o devolver datos


print("\n#### Ejemplo 6 ####")

def calculadora(valor1, valor2, basicas = False):
    
    multi = valor1 * valor2
    division = valor1 / valor2
    resta = valor1 - valor2
    sumar = valor1 + valor2

    cadena = ""
    if basicas !=False:
        cadena +="Suma: " + str(sumar)
        cadena += "\n"
        cadena += "Resta: "+ str (resta)
        cadena += "\n"
    else:
        cadena +="Division: " + str(division)
        cadena += "\n"
        cadena +="Multiplicacion: " + str(multi)
    return cadena

print(calculadora(5, 5, True))

# Ejemplo 7 funciones dentro de otras funciones


print("\n#### Ejemplo 7 ####")

def getNombre(nombre):
    texto =f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto =f"El nombre es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Pablo", "Vadecaveye"))

# Ejemplo 8 funciones lambda

print("\n#### Ejemplo 8 ####")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2021))

