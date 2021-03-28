# Importar modulo

import sqlite3
from typing import Counter

# Conexion

conexio = sqlite3.connect("./19-base.datos/pruebas.db")

#Crear un cursos

cursor = conexio.cursor()

# Crear una tabla

cursor.execute("CREATE TABLE IF NOT EXISTS productos ("+ 
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHARD (255),"+
"descripcion text,"+
"precio int (255)"+
")")
# Para guardar cambios 
conexio.commit()


# Insertar datos
#cursor.execute ("INSERT INTO productos VALUES (null,'Segundo producto','Descripcion de mi producto', 550)")

#conexio.commit()

#Cargar multiples productos a la tabla productos

productos = [
    ("Ordenador portatil", "buen PC", 700),
    ("telefono", "buen PC", 200),
    ("tablet portatil", "buena tablet", 400),
    ("Notebook", "buena note", 1700),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

conexio.commit()
# Update cambiar valores 

cursor.execute ("UPDATE productos SET precio=1900 WhERE precio=1700")
# Listar datos

#cursor.execute("SELECT * FROM productos;")

cursor.execute("SELECT * FROM productos WHERE precio >= 1500;")

productos = cursor.fetchall()

for producto in productos:
    print("Titulo:", producto[1])
    print("Descripcion:",producto [2])
    print("Precio:",producto[3])
    print("\n")
print(len(productos))

# primer registro de la tabla
cursor.execute("SELECT titulo FROM productos;")

producto = cursor.fetchone()
print (producto)

# cerrar la conexion

#conexio.close()


# Borrar registros de una tabla

cursor.execute ("DELETE FROM  productos ")

conexio.commit

conexio.close()
