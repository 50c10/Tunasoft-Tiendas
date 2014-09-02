from django import forms
from tienda.apps.ventas.models import producto, categoria

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Reset, Div, HTML


class addCartForm(forms.Form):
	idproducto = forms.IntegerField(widget=forms.HiddenInput())

class addProductForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_action = '.'
	helper.form_method ='POST'
	helper.layout = Layout (
		Fieldset(
			'Agregar Productos',
			'nombre',
			'precio',
			'stock',
			'descripcion',
			#Div(
			#	HTML("""<p>Aqui van las imagenes<p/>
			#			{% include "images/multiimage.html"%}
			#		""")
			#),
			'imagen',
			'categorias'
		),
		ButtonHolder (
			Submit('submit', 'Submit', css_class='button white'),
			Reset('Reset','Limpiar')
		)
	)

	class Meta:
		model = producto
		exclude = {'status', 'tienda',}
    
class addCategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        exclude = {'tienda',}

