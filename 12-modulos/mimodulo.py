def holaMundo(nombre):
    return f"Hola mundo como estas?, {nombre}"

def calculadora(valor1, valor2, basicas = False):
    
    multi = valor1 * valor2
    division = valor1 / valor2
    resta = valor1 - valor2
    sumar = valor1 + valor2

    cadena = ""
    if basicas !=False:
        cadena +="Suma: " + str(sumar)
        cadena += "\n"
        cadena += "Resta: "+ str (resta)
        cadena += "\n"
    else:
        cadena +="Division: " + str(division)
        cadena += "\n"
        cadena +="Multiplicacion: " + str(multi)
    return cadena