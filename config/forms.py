# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Este usuario no existe")
			if not user.check_password(password):
				raise forms.ValidationError("Password incorrecto")
			if not user.is_active:
				raise forms.ValidationError("Este usuario no esta activo")
		return super(UserLoginForm, self).clean(*args,**kwargs)

class UserRegister(forms.ModelForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}), validators=[RegexValidator(regex='^.{4,10}$', message='Este campo debe tener 4 a 10 carácteres', code='nomatch')])
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)', 'class': 'form-control'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellido(s)', 'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}), label='')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control'}), label='')
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password', 'password2']
	def clean_username(self):
		return self.cleaned_data.get('username').lower()
	def clean_first_name(self):
		return self.cleaned_data.get('first_name').title()
	def clean_last_name(self):
		return self.cleaned_data.get('last_name').title()
	def clean_password2(self):
		password2 =self.cleaned_data.get('password2')
		password = self.cleaned_data.get('password')
		if password2 != password:
			raise forms.ValidationError('Las contraseñas no coinciden')
