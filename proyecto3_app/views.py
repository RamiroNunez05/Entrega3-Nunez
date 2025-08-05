from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Familiar, Compra, Vuelo
from .forms import CompraForm, VueloForm, FamiliarForm

# Create your views here.

def home(request):
    return render( request, "proyecto3_app/home.html")

def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            familiar = Familiar(
                nombre=form.cleaned_data['nombre'],
                edad=form.cleaned_data['edad'],
                parentesco=form.cleaned_data['parentesco'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
            )
            familiar.save()
            return redirect('listar-familiares')

    form = FamiliarForm()
    return render(request, 'proyecto3_app/crear-familiar.html', {"form": form})

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

def buscar_compras(request):
    if request.method == 'GET':
        descripcion = request.GET.get('descripcion', '')
        compras = Compra.objects.filter(descripcion__icontains=descripcion)
        return render(request, 'proyecto3_app/ultimas-compras.html', {"compras": compras, "descripcion": descripcion})

def reservar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            vuelo = Vuelo(
            origen = form.cleaned_data['origen'],
            destino = form.cleaned_data['destino'],
            fecha_salida = form.cleaned_data['fecha_salida'],
            horario = form.cleaned_data['horario'],
            precio = form.cleaned_data['precio'],
        )
        vuelo.save()
        return redirect('vuelos-reservados')

    form = VueloForm()
    return render(request, 'proyecto3_app/reservar-vuelo.html', {"form": form})

def vuelos_reservados(request):
    vuelos = Vuelo.objects.all().order_by('-id')
    return render(request, 'proyecto3_app/vuelos-reservados.html', {"vuelos": vuelos})

def buscar_vuelos(request):
    if request.method == 'GET':
        destino = request.GET.get('destino', '')
        vuelos = Vuelo.objects.filter(destino__icontains=destino)
        return render(request, 'proyecto3_app/vuelos-reservados.html', {"vuelos": vuelos, "destino": destino})
