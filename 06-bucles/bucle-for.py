"""
# FOR

for variable in elemento_iterable (lista, rango etc)
    BLOQUE DE INSTRUCCIONES

Se va a ejecutar hasta que se acaben los elementos iterable que
pueden provenir de una lista, un rango etc..

# BREAK

break corta el bucle cuando se cumple una condicion
  
"""

contador = 0
resultado = 0
for contador in range (0, 100):
    print ("Voy por el: " + str (contador))
    
    resultado += contador 
    """ otra forma de escribir el codigo
    resultado = resultado + contador"""
print(f"El resultado es : {resultado}")


# Ejemplo tablas de multiplicar

print("\n########## EJEMPLO #########")

numero_usuario = int (input("¿ De que numero quieres la tabla?:"))


if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla de Multiplcar del numero: {numero_usuario} ####")

for numero_tabla in range (1, 11):
    if numero_usuario == 45:
        print ("No se puede mostrar numeros prohibidos!!")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")

else:
    print("\nTabla finalizada")