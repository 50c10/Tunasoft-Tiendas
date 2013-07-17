from django import forms

class ContactoForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput)
	Titulo = forms.CharField(widget=forms.TextInput)
	Texto = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	
class RegistroForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput, error_messages={'required': 'Este campo es nesesario!','invalid': 'esta dirrecion de e-mail no es valida'})
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),error_messages={'required': 'Este campo es nesesario!'})
	password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),error_messages={'required': 'Este campo es nesesario!'})
	tienda = forms.CharField(widget=forms.TextInput,error_messages={'required': 'Este campo es nesesario!'})