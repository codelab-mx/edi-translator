# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from .forms import NewPartnerForm, NewAddressForm
from .models import Company_Data, Partner_Data
from . import models

################################
#  MOSTRAR SOCIOS COMERCIALES  #
################################
@login_required (login_url='/login/')
def tradings_index(request):
	companies = models.Company_Data.objects.all()
	partners = models.Partner_Data.objects.all()
	return render(request, 'address/view.html', {'companies':companies, 'partners':partners})

#########################################
#  AGREGAR NUEVA DIRECCIÓN EMPRESARIAL  #
#  SE REQUIERE IMPORTAR NewAddressForm  #
#########################################
@permission_required('address.add_company_data', login_url='/')
@login_required (login_url='/login/')
def new_company(request):
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
		return HttpResponseRedirect(reverse('view_tradings'))
	return render(request, 'address/new_company.html', {'form':form})

#########################################
#  AGREGAR NUEVO SOCIO COMERCIAL        #
#  SE REQUIERE IMPORTAR NewPartnerForm  #
#########################################
@permission_required('address.add_partner_data', login_url='/')
@login_required (login_url='/login/')
def new_partner(request):
	form = NewPartnerForm(request.POST or None)
	partner = Partner_Data()
	if form.is_valid(): 
		partner.P_Name = form.cleaned_data.get('P_Name')
		partner.P_Edi_Address = form.cleaned_data.get('P_Edi_Address')
		partner.P_E_mail = form.cleaned_data.get('P_E_mail')
		partner.P_Address = form.cleaned_data.get('P_Address')
		partner.P_Country = form.cleaned_data.get('P_Country')
		partner.P_City = form.cleaned_data.get('P_City')
		partner.P_ZIP = form.cleaned_data.get('P_ZIP')
		partner.P_Phone = form.cleaned_data.get('P_Phone')
		partner.save()
		return HttpResponseRedirect(reverse('view_tradings'))
	return render(request, 'address/new_partner.html', {'form':form})

#########################################
#      EDITAR DIRECCIÓN EMPRESARIAL     #
#  SE REQUIERE IMPORTAR NewPartnerForm  #
#########################################
@permission_required('address.change_company_data', login_url='/')
@login_required (login_url='/login/')
def edit_company(request, company_id):
	form = NewAddressForm(request.POST or None)
	Address = Company_Data.objects.filter(id__exact=company_id).last()
	if form.is_valid():
		address = Company_Data.objects.get(id__exact=company_id)
		address.C_Name = form.cleaned_data.get('C_Name')
		address.C_Address = form.cleaned_data.get('C_Address')
		address.C_City = form.cleaned_data.get('C_City')
		address.C_Country = form.cleaned_data.get('C_Country')
		address.C_ZIP = form.cleaned_data.get('C_ZIP')
		address.C_E_mail = form.cleaned_data.get('C_E_mail')
		address.C_Phone	 = form.cleaned_data.get('C_Phone')		
		address.C_Edi_Address = form.cleaned_data.get('C_Edi_Address')
		address.save()
		return HttpResponseRedirect(reverse('view_tradings'))
	return render(request, 'address/edit_company.html', {'form':form, 'Address':Address})

#########################################
#         EDITAR SOCIO COMERCIAL        #
#  SE REQUIERE IMPORTAR NewPartnerForm  #
#########################################
@permission_required('address.change_partner_data', login_url='/')
@login_required (login_url='/login/')
def edit_partner(request, partner_id):
	form = NewPartnerForm(request.POST or None)
	Partner = Partner_Data.objects.filter(id__exact=partner_id).last()
	if form.is_valid(): 
		partner = Partner_Data.objects.get(id__exact=partner_id)
		partner.P_Name = form.cleaned_data.get('P_Name')
		partner.P_Edi_Address = form.cleaned_data.get('P_Edi_Address')
		partner.P_E_mail = form.cleaned_data.get('P_E_mail')
		partner.P_Address = form.cleaned_data.get('P_Address')
		partner.P_Country = form.cleaned_data.get('P_Country')
		partner.P_City = form.cleaned_data.get('P_City')
		partner.P_ZIP = form.cleaned_data.get('P_ZIP')
		partner.P_Phone = form.cleaned_data.get('P_Phone')
		partner.save()
		return HttpResponseRedirect(reverse('view_tradings'))
	return render(request, 'address/edit_partner.html', {'form':form, 'Partner':Partner})


#########################################
#         VER DIRECCIÓN EMPRESARIAL     #
#########################################
@permission_required('address.add_company_data', login_url='/')
@login_required (login_url='/login/')
def view_company(request, company_id):
	Address = Company_Data.objects.filter(id__exact=company_id).last()
	return render(request, 'address/view_company.html', {'Address':Address})

#########################################
#            VER SOCIO COMERCIAL        #
#########################################
@permission_required('address.add_partner_data', login_url='/')
@login_required (login_url='/login/')
def view_partner(request, partner_id):
	Partner = Partner_Data.objects.filter(id__exact=partner_id).last()
	return render(request, 'address/view_partner.html', {'Partner':Partner})


#########################################
#	 ELIMINAR DIRECCIÓN EMPRESARIAL     #
#########################################
@permission_required('address.delete_company_data', login_url='/')
@login_required (login_url='/login/')
def delete_company(request, company_id):
	Address = Company_Data.objects.filter(id__exact=company_id).last()
	Address.delete()
	return HttpResponseRedirect(reverse('view_tradings'))

#########################################
#	    ELIMINAR SOCIO COMERCIAL        #
#########################################
@permission_required('address.delete_partner_data', login_url='/')
@login_required (login_url='/login/')
def delete_partner(request, partner_id):
	Partner = Partner_Data.objects.filter(id__exact=partner_id).last()
	Partner.delete()
	return HttpResponseRedirect(reverse('view_tradings'))