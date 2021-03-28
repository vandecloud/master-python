import os
import shutil

# Crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya exsite el directorio")

# Borrar carpeta

#os.rmdir ("./mi_carpeta")

#Copiar
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta.COPIADA"

shutil.copytree(ruta_original, ruta_nueva)


# Borrar carpeta

#os.rmdir ("./mi_carpeta.COPIADA")
"""

print("Contenido de mi carpeta:")
contenido = os.listdir ("./mi_carpeta")

for ficheros in contenido:
    print(f"Ficheros:" + ficheros)

    
