# Si un dato cumple una condicion se va a ejecutar una accion y en caso de que no se cumple otra
"""
# Condicional IF

SI se cumple esta condicion:
    ejecutara grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones
    
if condicion:
    instrucciones
else:
    otras intrucciones

#Operadores de comparación
== igual
!= diferente
< mayor que
> menor que
<= menor o igual que
>= mayor o igual que

#Operadores logicos

and  Y
or   O
!    Negacion
not  NO

"""

# ejemplo 1

print("#########EJEMPLO1#########")
""""
# color = "rojo"
color = input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("el color es Rojo")
else:
    print("el color no es correcto")
"""
# ejemplo 2

print("\n#########EJEMPLO2#########")
"""
#year = 2020
year = int(input("Ingrese el Año: "))
if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es una año anterior a 2020")
"""
# ejemplo 3
print("\n#########EJEMPLO3#########")
"""
nombre = "Pablo Vandecaveye"
ciudad = "Buenos Aires"
continente = "America"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")
    if continente != "America":
        print("El usuario NO es Americano")
    else:
        print(f"Es Americano y de la ciudad de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")
"""

# ejemplo 4
"""
Evaluar condiciones con elif

"""
"""
print("\n#########EJEMPLO4#########")

dia = int(input("Introducir el dia de la semana: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print ("Es martes")
elif dia == 3:
    print ("Es Miercoles")
else:
    print ("El resto de la semana")
"""
# ejemplo 5
print("\n#########EJEMPLO5#########")
"""
edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Introdicir la edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar!!")
else:
    print("No esta en edad de trabajar")
"""
# ejemplo 6
print("\n#########EJEMPLO6#########")

pais = "Mexico"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es una pais de habla hispana!!")
else:
    print(f"El {pais} no es un pais de habla hispana!!")
   
# ejemplo 7
print("\n#########EJEMPLO7#########") 

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es una pais de habla hispana!!")
else:
    print(f"{pais} SI es un pais de habla hispana!!")
    
# ejemplo 8
print("\n#########EJEMPLO8#########")

pais = "Colombia"

if  (pais != "Mexico" and pais != "España" and pais != "Colombia"):
    print(f"{pais} NO es una pais de habla hispana!!")
else:
    print(f"{pais} SI es un pais de habla hispana !! :)")