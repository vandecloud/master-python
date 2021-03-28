from django.shortcuts import redirect, render, HttpResponse

# Create your views here.


layout = """

<h1> Sitio Web con Django | Pablo Vandecaveye </h1>


<hr/>

<ul>
    <li>
        <a href="/inicio"> Inicio </a> 
    </li>

    <li> 
        <a href="/hola_mundo"> Hola Mundo </a>
    </li>

    <li> 
        <a href="/pagina"> Pagina de Pruebas </a>
    </li>

    <li> 
        <a href="/contacto"> Pagina de Contactos </a>
    </li>

</ul>


<hr/>

"""



def index(request):
    """
    html = 
        <h1> Inicio </h1>
        <p> Año hasta el 2050 </p>
        <ol>
    
    
    year = 2021

    while year <=2050:
        if year %2 == 0:
            html += f"<li> {str(year)}</li>"
        year +=1 

    html += "<ol>"
    """
    year = 2021
    hasta = range ( year, 2051)

    nombre = 'Pablo Vandecaveye'
    lenguajes = ['JavaScript', 'python', 'PHP', 'C']
   

    return render(request, 'index.html',{
        'title' : 'Inicio',
        'nombre' : nombre,
        'mi_variable' : 'Soy un dato que esta en las vistas (views)',
        'lenguajes' : lenguajes,
        'years' : hasta
    })
    

def hola_mundo(request):
    return render (request, 'hola_mundo.html')




def pagina(request, redirigir=0):
    
    if redirigir == 1:
        return redirect ('https://google.com.ar')

    return render (request, 'pagina.html',{
        'texto' : ''
    }) 



def contacto(request, nombre, apellidos):
    return HttpResponse (layout+ f"h2> Pagina de Contactos {nombre} {apellidos} </h2>")



# Parametros opciones (Nombre Apellido )
"""
def contacto(request, nombre ="", apellidos = ""):
    html= ""

    if nombre and apellidos :
        html += "<p>Nombre Completo es:</p>"
        html += f"<h3> {nombre} {apellidos} </h3>"
        

    return HttpResponse (layout+ f"<h2> Pagina de Contactos</h2>"+ html )
"""

