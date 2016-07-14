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
verificamos que existan grupos en la base de datos para que no haya errores
obtenemos todos los usuarios de la base de datos con users
'''
def usuarios(request):
	is_admin = request.user.has_perm('auth.change_user')
	if is_admin == True and request.user.is_active:
		groups = Group.objects.all()
		users = User.objects.exclude(is_superuser=1).all()
		return render(request, 'usuarios/usuarios.html', {'users':users, 'groups':groups})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

##########################
#  REGISTRO DE USUARIOS  #
##########################
'''
Los usuarios administradores que puedan añadir usuarios pueden acceder a este apartado
is_admin filtra si el usuario puede añadir usuarios
group filtra que exista el grupo que se desea añadir 
Primer if verifica que todas las condiciones sean satisfactorias
form se conecta con forms.py, la renderiza en el template 
si el formulario es satisfactorio user.save() guarda el usuario, user.groups.add lo añade al grupo
Return carga la plantilla nuevo.html del template
si el usuario no está activo cierra la sesión
si ninguna condicion se cumple redirige a usuarios
'''
def usuario_nuevo(request, grupo):
	is_admin = request.user.has_perm('auth.add_user')
	group = Group.objects.filter(name=grupo).count()
	if is_admin == True and group == 1 and request.user.is_active:
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user.groups.add(Group.objects.get(name=grupo))
			return HttpResponseRedirect("/usuarios")
		return render(request, 'usuarios/nuevo.html', {'form':form, 'group':group, 'grupo':grupo})
	#if request.user.is_authenticated():
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/usuarios/")

###########################
#  EDITAR / VER USUARIOS  #
###########################
'''
is admin = verifica que el usuario sea administrador
primer if verifica que el usuario esté activo y le da acceso
	user = renderiza el perfil del usuario
	user_c = cuenta cuantos perfiles existen
	return = carga la plantilla correspondiente y manda la información de usuarios al template
elif si el usuario no está activo lo saca de la sesión
si alguna condición no se cumple renderiza raiz
'''
def ver_usuario(request, user_name):
	is_admin = request.user.has_perm('auth.change_user')
	if is_admin == True and request.user.is_active:
		user = User.objects.filter(username=user_name).exclude(is_superuser=1)
		return render(request, 'usuarios/perfil.html', {'user':user, 'user_name':user_name})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")
