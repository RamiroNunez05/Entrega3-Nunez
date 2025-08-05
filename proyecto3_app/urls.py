from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('crear-familiar/', views.crear_familiar, name='crear-familiar'),
        path('listar-familiares/', views.listar_familiares, name='listar-familiares'),
        path('compra/', views.comprar, name='compra'),
        path('ultimas-compras/', views.ultimas_compras, name='ultimas-compras'),
        path('buscar-compras/', views.buscar_compras, name="buscar-compras"),
        path('reservar-vuelo/', views.reservar_vuelo, name="reservar-vuelo"),
        path('vuelos-reservados/', views.vuelos_reservados, name="vuelos-reservados"),
        path('buscar-vuelos/', views.buscar_vuelos, name="buscar-vuelos"),
]