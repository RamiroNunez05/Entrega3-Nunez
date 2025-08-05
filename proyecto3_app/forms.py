from django import forms

class CompraForm(forms.Form):
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    precio = forms.FloatField(label='Precio')
    cantidad = forms.IntegerField(label='Cantidad')

