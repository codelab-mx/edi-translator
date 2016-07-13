# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from .forms import UserRegisterForm


#########################
#  VISUALIZAR USUARIOS  #
#########################
'''
Solamente los usuarios administradores podrán acceder a este apartado
is_admin es una variable que nos permite filtrar si el usuario es administrador

'''
def usuarios(request):
	#global is_admin
	is_admin = request.user.groups.filter(name='administrador').exists()
	#is_admin(request)
	if (is_admin == 1 or request.user.is_superuser) and request.user.is_active:
		groups = Group.objects.all()
		users = User.objects.exclude(is_superuser=1).all()
		return render(request, 'usuarios/usuarios.html', {'users':users, 'groups':groups, 'is_admin': is_admin})
	elif (is_admin == 1 or request.user.is_superuser) and not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

##########################
#  REGISTRO DE USUARIOS  #
##########################

def usuario_nuevo(request, grupo):
	is_admin = request.user.groups.filter(name='administrador').count()
	group = Group.objects.filter(name=grupo).count()
	if (request.user.is_superuser or is_admin == 1) and (group == 1 and request.user.is_active):
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user.groups.add(Group.objects.get(name=grupo))
			return HttpResponseRedirect("/usuarios")
		return render(request, 'usuarios/nuevo.html', {'form':form, 'group':group, 'grupo':grupo})
	elif (request.user.is_superuser or is_admin == 1) and (group == 1 and not request.user.is_active):
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/usuarios")

#####################
#  EDITAR USUARIOS  #
#####################


def ver_usuario(request, id):
	admin = User.objects.filter(id=id, is_superuser=1).count()
	if request.user.is_authenticated() and admin == 0:
		is_admin = request.user.groups.filter(name='administrador').exists()
		user = User.objects.filter(id=id).exclude(is_superuser=1)
		return render(request, 'usuarios/perfil.html', {'user':user, 'is_admin': is_admin, 'admin':admin})
	elif request.user.is_authenticated() and admin == 1:
		return render(request, '404.html')
	else:
		return HttpResponseRedirect("/")