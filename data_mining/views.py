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
			print new_file.id
			new_file.save()
			return HttpResponseRedirect('/edi')
		#elif:
		#form = DocumentForm()
		return render(request, 'EDI/traducir.html', {'form': form})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")
