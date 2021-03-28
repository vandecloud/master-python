#from logging import root
import mysql.connector
import datetime
import hashlib

from mysql.connector import cursor
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect [1]

class Usuario:
    
        def __init__(self, nombre, apellidos, email, password):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
            self.password = password
        
        def registrar(self):
            fecha = datetime.datetime.now()
            
            #Cifrar contraseña
            
            cifrado = hashlib.sha256()
            cifrado.update(self.password.encode('utf8'))
            
            sql = "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)"
            usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
            
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
    
        def identificar(self):
            
            # Consulta para comprobar si existe el usuarios
            sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "
            
            # Cifrado contraseña
            cifrado = hashlib.sha256()
            cifrado.update(self.password.encode('utf8'))
            
            # Datos para la consulta
            usuario = (self.email, cifrado.hexdigest())
            
            cursor.execute(sql, usuario)
            
            result = cursor.fetchone()
            
            return result