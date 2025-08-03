from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('hola/', views.hola, name='hola'),
        path('crear-familiar/<str:nom>', views.crear_familiar, name='crear-familiar'),
]