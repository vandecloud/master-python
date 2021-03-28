"""
Crear un programa que compruebe si una variable esta vacia y si esta
vacias rellenarlo con texto en minuscula y mostrarla en mayuscula
"""

texto = "Hola"

if len(texto.strip()) <=0 : # Comprueba si la variable texto contiene informacion a su vez suprime los espacios
    texto = " hola soy un texto en minusculas trasformado"
    print(texto.upper())
else:
    print(f"La variable tiene contenido: '{texto}'")