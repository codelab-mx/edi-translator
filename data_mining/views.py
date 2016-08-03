# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from forms import DocumentForm
from models import data_segments_master, data_segments_BFR, data_segments_N, data_segments_830LIN, data_segments_FST, data_segments_SHP
from . import models
from django.contrib import messages
from data import init_data
import datetime
#############################
#  VISUALIZAR ARCHIVOS EDI  #
#############################
'''
Solamente los usuarios administradores podrán acceder a este apartado
is_admin es una variable que nos permite filtrar si el usuario es administrador
@permission_required('polls.can_vote')
@permission_required('polls.can_vote', login_url='/loginpage/')
'''
@login_required
def edi_index(request):
	if request.user.is_active:
		edi_files = models.edi_address.objects.all()
		return render(request, 'EDI/ver.html', {'edi_files':edi_files})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

################
#  EDI VIEWER  #
################

@login_required
def edi_viewer(request, edi_viewer):
	edi = models.edi_address.objects.get(id=edi_viewer)
	file_name = edi.filename
	master = models.data_segments_master.objects.get(id=edi_viewer)
	s_1 = master.GS_4
	date_master = datetime.datetime.strptime(s_1, "%Y%m%d").date()
	bfr = master.data_segments_bfr_set.all()
	name = master.data_segments_n_set.all()
	shps = 1
	lin830 = master.data_segments_830lin_set.all()
	lin862 = master.data_segments_862lin_set.all()
	fst = master.data_segments_fst_set.all()
	return render(request, 'EDI/viewer.html', {'shps':shps, 'edi':edi, 'master':master, 'bfr':bfr, 'name':name, 'lin862':lin862, 'lin830':lin830, 'fst':fst, 'date_master':date_master})

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

#########################################
#  FORMULARIO PARA EDITAR ARCHIVOS EDI  #
#########################################

@login_required
def edi_information_editor(request, edi_editor):
	if request.user.is_active:
		info = models.edi_address.objects.get(edi_file=('edi/{}').format(edi_editor))
		print info
		return render(request, 'EDI/editar.html', {'info':info})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")



########################################
#  FORMULARIO PARA SUBIR ARCHIVOS EDI  #
########################################

@login_required
def edi_translator(request):
	if request.user.is_active:
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			new_file = models.edi_address(edi_file = request.FILES['docfile'])
			new_file.save()
			print new_file.id
			return HttpResponseRedirect(('{}').format(new_file.id))
		return render(request, 'EDI/traducir.html', {'form': form})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")

#################################
#  TRADUCCIÓN DE  ARCHIVOS EDI  #
#################################
@login_required
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
			return HttpResponseRedirect("/edi/")
		else:
			return HttpResponseRedirect("/edi/")
	return render(request, 'EDI/traducir.html', {'edi_files':edi_files})
