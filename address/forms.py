# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from .models import Partner_Data, Company_Data

class NewPartnerForm(forms.ModelForm):
	P_Name = forms.CharField(label='Nombre o Razón Social', widget=forms.TextInput(attrs={'placeholder': 'Nombre Comercial', 'class': 'form-control'}))
	P_Edi_Address = forms.CharField(label='Dirección EDI', widget=forms.TextInput(attrs={'placeholder': 'Dirección EDI', 'class': 'form-control'}))
	P_E_mail	= forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'placeholder': 'E-Mail', 'class': 'form-control'}))
	P_Address = forms.CharField(required=False, label='Dirección Física', widget=forms.TextInput(attrs={'placeholder': 'Dirección Física', 'class': 'form-control'}))
	P_Country = forms.CharField(required=False, label='País', widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
	P_City = forms.CharField(required=False, label='Ciudad', widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control'}))
	P_ZIP = forms.CharField(required=False, label='Código Postal', widget=forms.TextInput(attrs={'placeholder': 'Código Postal', 'class': 'form-control'}))
	P_Phone = forms.CharField(required=False, label='Teléfono', widget=forms.TextInput(attrs={'placeholder': 'Teléfono', 'class': 'form-control'}))
	class Meta:
		model = Partner_Data
		fields = ['P_Name', 'P_Edi_Address', 'P_Country', 'P_City', 'P_ZIP', 'P_E_mail', 'P_Phone', 'P_Address']
class NewAddressForm(forms.ModelForm):
	C_Name = forms.CharField(label='Nombre o Razón Social', widget=forms.TextInput(attrs={'placeholder': 'Nombre Comercial', 'class': 'form-control'}))
	C_Address = forms.CharField(required=False, label='Dirección Física', widget=forms.TextInput(attrs={'placeholder': 'Dirección Física', 'class': 'form-control'}))
	C_City = forms.CharField(required=False, label='Ciudad', widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control'}))
	C_Country = forms.CharField(required=False, label='País', widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
	C_ZIP = forms.CharField(required=False, label='Código Postal', widget=forms.TextInput(attrs={'placeholder': 'Código Postal', 'class': 'form-control'}))
	C_E_mail = forms.CharField(required=False, label='E-Mail', widget=forms.TextInput(attrs={'placeholder': 'E-Mail', 'class': 'form-control'}))
	C_Phone = forms.CharField(required=False, label='Teléfono', widget=forms.TextInput(attrs={'placeholder': 'Teléfono', 'class': 'form-control'}))
	C_Edi_Address = forms.CharField(label='Dirección EDI', widget=forms.TextInput(attrs={'placeholder': 'Dirección EDI', 'class': 'form-control'}))
	class Meta:
		model = Company_Data
		fields = ['C_Name', 'C_Edi_Address', 'C_Country', 'C_City', 'C_ZIP', 'C_E_mail', 'C_Phone', 'C_Address']