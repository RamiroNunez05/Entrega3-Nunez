from django import forms

class CompraForm(forms.Form):
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    precio = forms.FloatField(label='Precio')
    cantidad = forms.IntegerField(label='Cantidad')

class VueloForm(forms.Form):
    origen = forms.CharField(widget=forms.Textarea, label='Origen')
    destino = forms.CharField(widget=forms.Textarea, label='Destino')
    fecha_salida = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Salida')
    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Horario')
    precio = forms.FloatField(label='Precio')

