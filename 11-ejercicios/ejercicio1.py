"""
Hacer un prgrama que tenga una lista de 8 numeros enteros y haga
lo siguiente:
-Recorrer la lista y mostrala
- hacer funcion que recorra listas de numeros y devuelva un string
-Ordenarla y Mostrarla
-Mostrar su logitud
-Buscar algun elemento (que el usuario pida por teclado)

"""
"""
lista = []
lista_numero = ""
while lista_numero != 0:
    lista_numero =int(input(f"Introducir numeros aleatorios:"))
    lista.append(lista_numero)

for recorrido in lista:
    print(recorrido)

print(f"Contiene N° {len(lista)} elementos")

print(lista)
"""

# Crear lista

numeros = [1, 5, 8, 55, 99, 66, 99]

# funcion Recorrer y mostar
"""
def recorridoLista(lista):
    resultado = "" #Variable donde almaceno los bucles

    for elementos in lista:# Listo los elementos que estan en la varible lista
          resultado += "Elemento:"  + str(elementos)#por cada elemento agrego al resultado la informacion obtenida de la lista
          resultado += "\n"
    return resultado #devuelvo el resultado 

print(recorridoLista(numeros))#invoco mi funcion y le paso la lista de elemenos 
print(recorridoLista(["Juan", "Pedro"]))# le puedo pasar cual lista, es la ventaja de usar funcion
"""
def recorridoLista(lista):
    # Variable que se incrementa 
    resultado = "" 
    # Ciclo que recorre la Lista
    for elementos in lista:
          resultado += "Elemento:"  + str(elementos)
          resultado += "\n"
    return resultado 

print(recorridoLista(numeros)) 

# Ordena y Mostrar

numeros.sort()
print(recorridoLista(numeros))

# Mostrar su logitud

print(f"Contiene {len(numeros)} elementos")

#Busqueda en la lista
"""
busqueda = int(input("Introduce el numero a buscar: "))
comprobar = isinstance(busqueda, int)# Comprobar que el elemento ingresado por el usuario es un entero

while not comprobar or busqueda <=0:# Ciclo While hasta tanto se cumpla la condicion (Busqueda o comprobar sea mayor a 0) 
    busqueda = int(input("Introduce el numero a buscar: "))# Volvera a solicitar incluir el valor a buscar hasta que se cumpla la condicion
else:
    print(f" Has introducido el numero:  {busqueda}")  
try:
    searh = numeros.index(busqueda)  #Realiza la busqueda del elemento dentro de la lista
    print(f"El numero buscado existe en la lista es el indice:  {searh}")
except:
    print("El numero no esta en la lista")
"""
# Multiple excepciones
try:
    numero = int(input("Introduce un valor: "))
    print(f"El cuadrado de {numero} es: " + str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros")
#except ValueError:
    print ("Introduce un numero correcto!!")
except Exception as e:
    print("ha ocurrido un error:", type(e).__name__)

# Excepcines personalizadas o lanzar excepciones
try:
    nombre = input( "Introduce el Nombre:")
    edad = int (input("Introduce la edad:"))

    if edad < 5 or edad >110:
        raise ValueError ("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError ("El nombre no esta completo")
    print (f"Bienvenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente!!")
except Exception as e:
    print("Existe un error:", e)


