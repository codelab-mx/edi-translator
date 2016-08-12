# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
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
@permission_required('auth.add_user', login_url='/tradings/')
@login_required(login_url='/login/')
def usuarios(request):
	groups = Group.objects.all()
	users = User.objects.exclude(is_superuser=1).all()
	return render(request, 'usuarios/usuarios.html', {'users':users, 'groups':groups})
	
##########################
#  REGISTRO DE USUARIOS  #
##########################
@permission_required('auth.add_user', login_url='/usuarios/')
@login_required (login_url='/login/')
def usuario_nuevo(request, grupo):
	group = Group.objects.filter(name=grupo).count()
	if group == 1:
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user.groups.add(Group.objects.get(name=grupo))
			return HttpResponseRedirect("/usuarios")
		return render(request, 'usuarios/nuevo.html', {'form':form, 'group':group, 'grupo':grupo})
	else:
		return HttpResponseRedirect("/usuarios/")

###########################
#  EDITAR / VER USUARIOS  #
###########################
@permission_required('auth.change_user', login_url='/usuarios/')
@login_required (login_url='/login/')
def ver_usuario(request, user_name):
	user = User.objects.filter(username=user_name).exclude(is_superuser=1)
	return render(request, 'usuarios/perfil.html', {'user':user, 'user_name':user_name})