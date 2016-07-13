# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render

#############################
#  VISUALIZAR ARCHIVOS EDI  #
#############################
'''
Solamente los usuarios administradores podrán acceder a este apartado
is_admin es una variable que nos permite filtrar si el usuario es administrador

'''
def edi_index(request):
	if request.user.is_active:
		groups = Group.objects.all()
		return render(request, 'EDI/ver.html', {})
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
		groups = Group.objects.all()
		return render(request, 'EDI/traducir.html', {})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")