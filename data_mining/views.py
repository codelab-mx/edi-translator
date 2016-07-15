# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from forms import DocumentForm
from models import edi_address
from . import models
from data import init_data
#############################
#  VISUALIZAR ARCHIVOS EDI  #
#############################
'''
Solamente los usuarios administradores podrán acceder a este apartado
is_admin es una variable que nos permite filtrar si el usuario es administrador

'''
def edi_index(request):
	if request.user.is_active:
		edi_files = models.edi_address.objects.all()
		return render(request, 'EDI/ver.html', {'edi_files':edi_files})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")


##########################
#  GENERAR ARCHIVOS EDI  #
##########################
'''
Solamente los usuarios administradores podrán acceder a este apartado
is_admin es una variable que nos permite filtrar si el usuario es administrador

'''
def edi_generator(request):
	if request.user.is_active:
		groups = Group.objects.all()
		return render(request, 'EDI/generar.html', {})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

def edi_translator(request):
	if request.user.is_active:
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			new_file = edi_address(edi_file = request.FILES['docfile'])
			new_file.save()
			print new_file.id
			return HttpResponseRedirect(('{}').format(new_file.id))
		return render(request, 'EDI/traducir.html', {'form': form})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

def edi_translate(request, edi):
	if request.user.is_active:
		edi_files = models.edi_address.objects.filter(id=edi)
		for edi in edi_files:
			id_edi_local = edi.id
			address_local = edi.edi_file
			flag_local = edi.flag
		if flag_local == False:
			print 'id_edi_local', id_edi_local
			init_data(id_edi_local, address_local, flag_local)
		else:
			return HttpResponseRedirect("/edi/")	
	return render(request, 'EDI/traducir.html', {'edi_files':edi_files})
