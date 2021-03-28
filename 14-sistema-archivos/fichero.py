from io import open #Modulo io dentro de Open
import pathlib #Libreria que te permite pasar la ruta absoluta de un archivo
import shutil # Modulo copiar renombrar archivos
import os # Modulo para remover archivo
import os.path #Comprobar si existe una ruta

"""

#Abrir archivo con ruta absoluta
ruta =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir
archivo.write("************Soy un texto*************\n")

#cerrar archivo

archivo.close()

#Leer contenido
ruta =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo en lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista)

for elementos in lista:
    if elementos.isnumeric():
     print("-" + elementos.upper())
    else:
         print(len(elementos), (elementos) )

#Copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva =str(pathlib.Path().absolute()) + "/copia_fichero_texto.txt"
#ruta_alternativa = "./07-ejercicios/copia_fichero_texto.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""
# Mover renombrar
"""
ruta_original = str(pathlib.Path().absolute()) + "/copia_fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/copia_fichero_NUEVA.txt"

shutil.move(ruta_original, ruta_nueva)

# Eliminar ficheros

ruta_nueva = str(pathlib.Path().absolute()) + "/copia_fichero_NUEVA.txt"

os.remove(ruta_nueva)
"""
#Comprobar si existe un archivo 
"""
print (os.path.abspath("./")) # Ruta absoluta
ruta_comprobar = (os.path.abspath("./") + "/fichero_texto.txt")
if os.path.isfile(ruta_comprobar):
    print("El fichero exite")
else:
    print("El fichero no existe")
"""





