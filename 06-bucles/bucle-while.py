"""
# BUCLE WHILE

While es una estructura de contro que intera o repite la ejecucion de
una serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condicion.

while condicion:
        bloquede instrcciones
        actualizacion del contador

"""
#Ejercicio 1
print ("\n#### EJERCICIO 01 ####")

contador = 1

while contador <=2:
    print(f"Estoy en el numero: {contador}")
    contador += 1

# Ejercicio 2
print ("\n#### EJERCICIO 02 ####")

contador = 1
muestrame = str()

while contador <=10:
    muestrame = muestrame + "," + str(contador)
    print(f"Estoy en el numero: {contador}")
    contador += 1

print(muestrame)

#Ejercicio 3
print ("\n#### EJERCICIO 03 ####")

numero_usuario = int (input("¿de que numero quieres en la tabla?"))

if numero_usuario < 1:
    numero_usuario =1

print(f"###Tabla del {numero_usuario}###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}") 
    contador += 1
else:
    print(f"Tabla Terminada")
