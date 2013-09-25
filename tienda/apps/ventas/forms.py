from django import forms
from tienda.apps.ventas.models import producto, categoria

class addProductForm(forms.ModelForm):
    class Meta:
        model = producto
        exclude = {'status', 'tienda',}
    
class addCategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        exclude = {'tienda',}
    