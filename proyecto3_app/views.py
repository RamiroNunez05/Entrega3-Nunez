from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Familiar, Compra
from .forms import CompraForm

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
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = Compra(
            descripcion = form.cleaned_data['descripcion'],
            precio = form.cleaned_data['precio'],
            cantidad = form.cleaned_data['cantidad'],
        )
        compra.save()
        return redirect('ultimas-compras')

    form = CompraForm()
    return render(request, 'proyecto3_app/tienda-compra.html', {"form": form})

def ultimas_compras(request):
    compras = Compra.objects.all().order_by('-id')
    return render(request, 'proyecto3_app/ultimas-compras.html', {"compras": compras})