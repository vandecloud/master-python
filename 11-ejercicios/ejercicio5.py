"""
Crear una lista con el contenido de esta tabla:

ACCION         AVENTURA                DEPORTES

GTA            ASSINS                  FIFA 21
COD            CRASH                   PRO 21
PUGB           Prince of persia        MOTO GP 21

Mostrar esta informacion ordenada

"""

tabla = [
    {
        'categoria': 'ACCION',
        'juegos': ['GTA', 'COD', 'PUGB']
    },
    {
        'categoria': 'AVENTURA',
        'juegos': ['ASSINS', 'CRASH', 'Prince of persia']
    },
    {
        'categoria': 'DEPORTE',
        'juegos': ['FIFA 21', 'PRO 21', 'MOTO GP 21']
    },
]

for categoria in tabla:
    print (f"------------------ {categoria['categoria']}------------------")
    for juegos in categoria ['juegos']:
        print (f"{juegos}")