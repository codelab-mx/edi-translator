# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login, get_user_model
#from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.contrib.auth.models import User, Group
from .forms import UserLoginForm, UserRegister

def home(request):
	#if request.user.is_authenticated() and request.user.is_active:
	if request.user.is_active:
		return render(request, 'index/index.html', {})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/login/")

def login_crm(request):
	try:
		group = Group.objects.get(name='administrador').user_set.all().count()
	except Group.DoesNotExist:
		group = 0
	if group == 0:
		return HttpResponseRedirect("/setup")
	elif request.user.is_active:
		return HttpResponseRedirect("/")
	else:
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect("/")
		return render(request, 'auth/login.html', {"form":form})

def logout_crm(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/login/")

def setup(request):
	admins = Group.objects.get(name="administrador").user_set.all().count()
	if admins == 0:
		reg_form = UserRegister(request.POST or None)
		if reg_form.is_valid():
			user = reg_form.save(commit=False)
			password = reg_form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user.groups.add(Group.objects.get(name='administrador'))
			return HttpResponseRedirect("/login")
		return render(request, 'auth/registro.html', {'reg_form':reg_form})
	else:
		return HttpResponseRedirect("/login")

	

def handler404(request):
	response = render_to_response('404.html', {}, context_instance = RequestContext(request))
	response.status_code = 404
	return response