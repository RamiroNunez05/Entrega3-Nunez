from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def home(request):
    return render( request, "proyecto3_app/home.html")

def hola(request):
    return HttpResponse("Hola Juan Carlos")

def crear_familiar(request, nom):
    if nom is not None:
        Familiar.objects.create(
            nombre=nom, edad=30, fecha_nacimiento="1995-02-02", parentesco="Hermano")
    return render(request, 'proyecto3_app/crear-familiar.html', {"familiar": nom})

def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'proyecto3_app/listar-familiares.html', {"familiares": familiares})

def comprar(request):
    pass