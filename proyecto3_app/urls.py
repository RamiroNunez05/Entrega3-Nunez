from django.urls import path
from . import views

urlpatterns = [
        path('hola-mundo/', views.hola_mundo, name='hola-mundo')
]