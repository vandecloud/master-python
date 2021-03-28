"""
Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el titulo de la tabla y luego las multiplicaciones

"""
for inicio in range(1, 11):
    print(f"TABLA {inicio}")

    for tabla in range (1,11):
        print(f"{tabla} x {inicio} = {tabla*inicio}")

