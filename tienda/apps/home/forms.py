from django import forms
from django.contrib.auth.models import User

class UserField(forms.CharField):
	def clean(self, value):
		super(UserField, self).clean(value)
		try:
			User.objects.get(username=value)
			raise forms.ValidationError("El usuario ya esta en uso. Intenta con otro.")
		except User.DoesNotExist:
			return value

class ContactoForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput)
	Titulo = forms.CharField(widget=forms.TextInput)
	Texto = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	
class RegistroForm(forms.Form):
	usuario = UserField(widget=forms.TextInput,error_messages={'required': 'Este campo es nesesario!'})
	Email = forms.EmailField(widget=forms.TextInput, error_messages={'required': 'Este campo es nesesario!','invalid': 'esta dirrecion de e-mail no es valida'})
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),error_messages={'required': 'Este campo es nesesario!'})
	password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),error_messages={'required': 'Este campo es nesesario!'})
	tienda = forms.CharField(widget=forms.TextInput,error_messages={'required': 'Este campo es nesesario!'})

	def clean_password(self):
		if self.data['password'] != self.data['password2']:
			raise forms.ValidationError('Los passwords no coinciden')
		return self.data['password']

	def clean(self,*args, **kwargs):
		self.clean_password()
		return super(RegistroForm, self).clean(*args, **kwargs)