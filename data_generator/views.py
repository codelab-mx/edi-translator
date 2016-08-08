# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ASN_Heading, ASN_Shipment, ASN_Order, ASN_Item
from models import Data_Generator_Master, Data_Generator_Hierarchial, Data_Generator_Order, Data_Generator_I_CLD
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from . import models

# Create your views here.
def ASN_New(request):
	global master
	form = ASN_Heading(request.POST or None)
	master = Data_Generator_Master()
	if form.is_valid():
		master.ST01 = "856"
		master.ST02 = form.cleaned_data.get('ST02')
		master.BST01 = form.cleaned_data.get('BST01')
		master.BST02 = "00"
		master.BST03 = form.cleaned_data.get('BST03')
		master.BST04 = form.cleaned_data.get('BST04')
		master.DTM01 = "011"
		master.DTM02 = form.cleaned_data.get('BST03')
		master.DTM03 = form.cleaned_data.get('BST04')
		master.DTM04 = form.cleaned_data.get('DTM04')
		master.DTM05 = "21"
		master.save()
		cont = 0
		print master.id
		return HttpResponseRedirect(('{}/shipment/{}/').format(master.id, cont))
	return render(request, 'EDI/generar/heading.html', {'form':form,})

def ASN_New_Shipment(request, master_id , cont):
	global master, hierarchial
	cont_integer = int(cont)
	cont_integer = cont_integer + 1

	master_files = models.Data_Generator_Master.objects.filter(id=master_id)
	for master_id in master_files:
		m_id = master.id
	hierarchial = Data_Generator_Hierarchial()
	form = ASN_Shipment(request.POST or None)
	if form.is_valid():
		hierarchial.PRIM = models.Data_Generator_Master.objects.get(id=m_id)
		hierarchial.HL01 = "1"
		hierarchial.HL02 = ""
		hierarchial.HL03 = "S"
		master.MEA01 = "PD"
		master.MEA02 = form.cleaned_data.get('MEA02')
		master.MEA03 = form.cleaned_data.get('MEA03')
		master.MEA04 = form.cleaned_data.get('MEA04')
		master.TD101 = form.cleaned_data.get('TD101')
		master.TD102 = form.cleaned_data.get('TD102')
		master.TD501 = "B"
		master.TD502 = "2"
		master.TD503 = form.cleaned_data.get('TD503')
		master.TD504 = form.cleaned_data.get('TD504')
		master.TD507 = form.cleaned_data.get('TD507')
		master.TD508= form.cleaned_data.get('TD508')
		master.TD301 = form.cleaned_data.get('TD301')
		master.TD302 = form.cleaned_data.get('TD302')
		master.TD303 = form.cleaned_data.get('TD303')
		master.TD401 = form.cleaned_data.get('TD401')
		master.TD402 = form.cleaned_data.get('TD402')
		master.TD403 = form.cleaned_data.get('TD403')
		master.TD404 = form.cleaned_data.get('TD404')
		master.TD405 = form.cleaned_data.get('TD405')
		master.REF01 = form.cleaned_data.get('REF01')
		master.REF01 = form.cleaned_data.get('REF01')
		master.save()
		hierarchial.save()
		return HttpResponseRedirect(('/crear/856/{}/order/{}/').format(master.id, cont_integer))
	return render(request, 'EDI/generar/shipment.html', {'form':form, 'master_files':master_files})


def ASN_New_Order(request, master_id, cont):
	global master, flag, contador
	flag = False
	contador = 2
	cont_integer = int(cont)
	cont_integer = cont_integer + 1
	master_files = models.Data_Generator_Master.objects.filter(id=master_id)
	for master_id in master_files:
		m_id = master.id
	hierarchial_order = Data_Generator_Hierarchial()
	order = Data_Generator_Order()
	form = ASN_Order(request.POST or None)
	if form.is_valid():
		hierarchial_order.PRIM = models.Data_Generator_Master.objects.get(id=m_id)
		hierarchial_order.HL01 = str(cont_integer)
		hierarchial_order.HL02 = "1"
		hierarchial_order.HL03 = "O"
		order.LIN02 = form.cleaned_data.get('LIN02')
		order.LIN03 = form.cleaned_data.get('LIN03')
		order.SN102 = form.cleaned_data.get('SN102')
		order.SN103 = form.cleaned_data.get('SN103')
		order.SN104 = form.cleaned_data.get('SN104')
		order.PRF01 = form.cleaned_data.get('PRF01')
		order.PRIM = models.Data_Generator_Master.objects.get(id=m_id)
		order.save()
		hierarchial_order.save()
		return HttpResponseRedirect(("/crear/856/{}/item/{}/").format(master.id, cont_integer))
	return render(request, 'EDI/generar/order.html', {'form':form,})

def ASN_New_Item(request, master_id, cont):
	global flag, contador
	print flag
	master_files = models.Data_Generator_Master.objects.filter(id=master_id)
	for master_id in master_files:
		m_id = master.id
	hierarchial_order = Data_Generator_Hierarchial()
	form = ASN_Item(request.POST or None)
	item_cld = Data_Generator_I_CLD()
	if form.is_valid():
		if flag == True:
			cont_integer = int(cont)
			cont_integer_mas = cont_integer + contador
			print cont_integer, contador
			contador = contador + 1
		else:
			cont_integer = int(cont)
			cont_integer_mas = cont_integer + 1
		hierarchial_order.PRIM = models.Data_Generator_Master.objects.get(id=m_id)
		hierarchial_order.HL01 = str(cont_integer_mas)
		hierarchial_order.HL02 = cont_integer
		hierarchial_order.HL03 = "I"
		hierarchial_order.CLD01 = form.cleaned_data.get('CLD01')
		hierarchial_order.CLD02 = form.cleaned_data.get('CLD02')
		hierarchial_order.CLD03 = form.cleaned_data.get('CLD03')
		hierarchial_order.save()
		if (request.POST.get('next')):
			return HttpResponseRedirect(('/crear/ver/{}').format(master.id))
		if (request.POST.get('order')):
			return HttpResponseRedirect(('/crear/856/{}/order/{}/').format(master.id, cont_integer_mas))
		if (request.POST.get('item')):
			flag = True
			return HttpResponseRedirect(('/crear/856/{}/item/{}/').format(master.id, cont_integer))


	return render(request, 'EDI/generar/item.html', {'form':form,})

def render_list(request):
	if request.user.is_active:
		edi_files = models.Data_Generator_Master.objects.all()
		return render(request, 'EDI/render/view-list.html', {'edi_files':edi_files})
	elif not request.user.is_active:
		return HttpResponseRedirect("/logout/")
	else:
		return HttpResponseRedirect("/")



def index_render(request, master_id):
	edi = models.Data_Generator_Master.objects.get(id=master_id)
	hl = Data_Generator_Hierarchial.objects.filter(PRIM_id=master_id)
	order = Data_Generator_Order.objects.filter(PRIM_id=master_id)
	return render(request, 'EDI/render/edi.html', {'edi':edi, 'hl':hl, 'order':order})


