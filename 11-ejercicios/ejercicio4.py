"""
Crear una script que tenga 4 variables una lista un string un entero y un booleano y 
que imprima un mensaje segun el tipo de dato de cada variable. usar funciones

"""

def traducirTipo (tipo):
    result = ''
    if tipo == list:
        result = 'LISTA'
    elif tipo == str:
        result = 'String'
    elif tipo == int:
        result = 'Entero'
    elif tipo == bool:
        result = 'Bool'
    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        print (f'Este dato es del tipo {traducirTipo(tipo)}')
    else:  
        result = 'El tipo de dato no es correcto'
    return result





mi_lista = ['hola mundo', 77, 'chau mundo']
titulo = 'Master en python'
numero = 100
verdadero = True


print (comprobarTipado (mi_lista, list))
print (comprobarTipado (titulo, str))
print (comprobarTipado (numero, int))
print (comprobarTipado (verdadero, bool))

"""
print(type(mi_lista))
print(type(titulo))
print(type(numero))
print(type(verdadero))
"""