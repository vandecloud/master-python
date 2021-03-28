"""
Crear un programa que solicite la nota a 15 alumnos y sacar por 
pantalla cuantos aprobaro y cuantos suspendieron

"""

contador = 1
desaprobado = 0
aprobado = 0

numero_alumnos = int(input(f"Introducir cuantos alumnos tiene: "))

while contador <= numero_alumnos:
    nota = int (input(f"Introducir la nota del alumnoS: "))
    if nota >= 7:
        aprobado += 1
    else:
        desaprobado+=1

    contador += 1

print(f"Cantidad de alumnos aprobados: ", aprobado)
print(f"Cantidad de alumnos desaprobados: ",desaprobado)