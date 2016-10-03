# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render
from forms import DocumentForm
from models import data_segments_master, data_segments_BFR, data_segments_N, data_segments_830LIN, data_segments_FST, data_segments_SHP, data_segments_ATH
from . import models
from django.contrib import messages
from data import init_data
from address.models import Partner_Data, Company_Data
import datetime, os

#############################
#  VISUALIZAR ARCHIVOS EDI  #
#############################
@permission_required('data_mining.add_edi_address', login_url='/tradings/')
@login_required(login_url='/login/')
def edi_index(request):
	edi_files = models.edi_address.objects.all().order_by('id').reverse()
	return render(request, 'EDI/ver.html', {'edi_files':edi_files})

################
#  EDI VIEWER  #
################
@permission_required('data_mining.add_edi_address', login_url='/')
@login_required (login_url='/login/')
def edi_viewer(request, edi_viewer):
	edi = models.edi_address.objects.get(id=edi_viewer)
	file_name = edi.filename
	master = models.data_segments_master.objects.get(id=edi_viewer)
	partner = Partner_Data.objects.filter(P_Edi_Address=master.GS_2)
	address = Company_Data.objects.filter(C_Edi_Address=master.GS_3)
	print master.GS_2
	print partner
	bfr = master.data_segments_bfr_set.all()
	name = master.data_segments_n_set.all()
	shps = master.data_segments_shp_set.all()
	ath = master.data_segments_ath_set.all()
	lin830 = master.data_segments_830lin_set.all()
	lin862 = master.data_segments_862lin_set.all()
	fst = master.data_segments_fst_set.all()
	return render(request, 'EDI/viewer.html', {'address':address, 'partner':partner, 'ath':ath, 'shps':shps, 'edi':edi, 'master':master, 'bfr':bfr, 'name':name, 'lin862':lin862, 'lin830':lin830, 'fst':fst})


########################################
#  FORMULARIO PARA SUBIR ARCHIVOS EDI  #
########################################
@permission_required('data_mining.add_edi_address', login_url='/')
@login_required (login_url='/login/')
def edi_translator(request):
	form = DocumentForm(request.POST, request.FILES)
	if form.is_valid():
		new_file = models.edi_address(edi_file = request.FILES['docfile'])
		new_file.save()
		print new_file.id
		return HttpResponseRedirect(('{}').format(new_file.id))
	return render(request, 'EDI/traducir.html', {'form': form})
	
#################################
#  TRADUCCIÓN DE  ARCHIVOS EDI  #
#################################
@permission_required('data_mining.add_edi_address', login_url='/')
@login_required (login_url='/login/')
def edi_translate(request, edi):
	edi_files = models.edi_address.objects.filter(id=edi)
	for edi in edi_files:
		id_edi_local = edi.id
		address_local = edi.edi_file
		flag_local = edi.flag
	if flag_local == False:
		init_data(id_edi_local, address_local, flag_local)
		return HttpResponseRedirect("/edi/")
	else:
		return HttpResponseRedirect("/edi/")
	return render(request, 'EDI/traducir.html', {'edi_files':edi_files})

##########################
#  BORRAR  ARCHIVOS EDI  #
##########################
@permission_required('data_mining.delete_edi_address', login_url='/logout/')
@login_required (login_url='/login/')
def delete_edi(request, edi):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	try:
		edi_files = models.edi_address.objects.get(id=edi)
		path = os.path.join(BASE_DIR, "media/{}".format(edi_files.edi_file))
		edi_files.delete()
		os.remove(path)
		return  HttpResponseRedirect("/edi/")
	except:
		return  HttpResponseRedirect("/edi/")
	return render(request, 'EDI/', {'edi_files':edi_files})
