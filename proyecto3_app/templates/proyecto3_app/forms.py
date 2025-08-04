from django import forms

class TiendaForm(forms.form):
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    precio = forms.FloatField(label='Precio')
    cantidad = forms.IntegerField(label='Cantidad')
