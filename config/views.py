# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.contrib.auth.models import User, Group
from .forms import UserLoginForm, UserRegister
import subprocess, os

@permission_required('data_mining.add_edi_address', login_url='/logout/')
@login_required (login_url='/login/')
def home(request):
	return HttpResponseRedirect("/tradings/")


def login_crm(request):
	users = User.objects.exclude(is_superuser=1).count()
	if users == 0:
		return HttpResponseRedirect("/setup")
	elif users >= 0 and request.user.is_active:
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

@login_required (login_url='/login/')
def logout_crm(request):
	logout(request)
	return HttpResponseRedirect("/login/")

def setup(request):
	s_u = User.objects.filter(is_superuser=1).count()
	users = User.objects.exclude(is_superuser=1).count()
	if s_u == 0:
		if(request.POST.get('mybtn')):
			a = int(request.POST.get('mytextbox'))
			if a == 1:
				BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
				command = "python {}/manage.py loaddata initial_data.json".format(BASE_DIR)
				process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
				output = process.communicate()[0]
				return HttpResponseRedirect("/login")
		return render(request, 'auth/setup.html', {})
	elif s_u >= 0 and users == 0:
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