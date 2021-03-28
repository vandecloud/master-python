""""
Proyecto python y Mysql:
- Abrir asistente
- Login o Registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntara 
- crear nota, mostrar notas, borrarlas.

"""
from usuarios import acciones

print ("""
Acciones disponibles:
    -Registro
    -Login
    """)

hazEl = acciones.Acciones()

accion = input ("¿ Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
    
elif accion == "login":
    hazEl.login()
    
    