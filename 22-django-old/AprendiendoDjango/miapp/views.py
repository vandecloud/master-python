from django.http import request
from django.shortcuts import render, HttpResponse

# Create your views here.

#MVC = Modelo Vista Controlador -> Acciones (metodos)
#MVT = Modelo Vista Template -> Acciones (metodos)


def index(request):
    return render (request, 'index.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render (request, 'pagina.html')

def contactos(request):
    return render (request, 'contactos.html')