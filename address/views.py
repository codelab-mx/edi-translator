# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.contrib.auth.models import User, Group
from .forms import NewPartnerForm, NewAddressForm
from .models import Company_Data, Partner_Data
from . import models

def tradings_index(request):
	companies = models.Company_Data.objects.all()
	partners = models.Partner_Data.objects.all()
	return render(request, 'address/view.html', {'companies':companies, 'partners':partners})

def new_company(request):
	if request.user.is_active:
		form = NewAddressForm(request.POST or None)
		address = Company_Data()
		if form.is_valid():
			address.C_Name = form.cleaned_data.get('C_Name')
			address.C_Address = form.cleaned_data.get('C_Address')
			address.C_City = form.cleaned_data.get('C_City')
			address.C_Country = form.cleaned_data.get('C_Country')
			address.C_ZIP = form.cleaned_data.get('C_ZIP')
			address.C_E_mail = form.cleaned_data.get('C_E_mail')
			address.C_Phone	 = form.cleaned_data.get('C_Phone')		
			address.C_Edi_Address = form.cleaned_data.get('C_Edi_Address')
			address.save()
			return HttpResponseRedirect("/tradings")
		return render(request, 'address/new_company.html', {'form':form})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")

def new_partner(request):
	if request.user.is_active:
		form = NewPartnerForm(request.POST or None)
		partner = Partner_Data()
		if form.is_valid(): 
			partner.P_Name = form.cleaned_data.get('P_Name')
			partner.DUNS = form.cleaned_data.get('DUNS')
			partner.P_Edi_Address = form.cleaned_data.get('P_Edi_Address')
			partner.P_E_mail = form.cleaned_data.get('P_E_mail')
			partner.P_Address = form.cleaned_data.get('P_Address')
			partner.P_Country = form.cleaned_data.get('P_Country')
			partner.P_City = form.cleaned_data.get('P_City')
			partner.P_ZIP = form.cleaned_data.get('P_ZIP')
			partner.P_Phone = form.cleaned_data.get('P_Phone')
			partner.save()
			return HttpResponseRedirect("/tradings")
		return render(request, 'address/new_partner.html', {'form':form})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")