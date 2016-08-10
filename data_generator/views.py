# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ASN_Heading, ASN_Shipment, ASN_Order, ASN_Item
from models import Data_Generator_Master, Data_Generator_Hierarchial, Data_Generator_Order
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from . import models
from address.models import Partner_Data, Company_Data
# Create your views here.
def ASN_New(request):
	global master
	form = ASN_Heading(request.POST or None)
	master = Data_Generator_Master()
	partner = Partner_Data.objects.all()
	address = Company_Data.objects.all()
	if form.is_valid():
		master.ST01 = "856"
		master.CLIENT = form.cleaned_data.get('CLIENT')
		master.NAME = form.cleaned_data.get('NAME')
		master.PREFIX_CLIENT = form.cleaned_data.get('PREFIX_CLIENT')
		master.PREFIX_NAME = form.cleaned_data.get('PREFIX_NAME')
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
	return render(request, 'EDI/generar/heading.html', {'form':form, 'partner':partner, 'address':address})

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
		master.N101 = form.cleaned_data.get('N101')
		master.N103 = form.cleaned_data.get('N103')
		master.N104 = form.cleaned_data.get('N104')
		master.N201 = form.cleaned_data.get('N201')
		master.N203 = form.cleaned_data.get('N203')
		master.N204 = form.cleaned_data.get('N204')
		master.N301 = form.cleaned_data.get('N301')
		master.N303 = form.cleaned_data.get('N303')
		master.N304 = form.cleaned_data.get('N304')
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
		hierarchial_order.LIN02 = form.cleaned_data.get('LIN02')
		hierarchial_order.LIN03 = form.cleaned_data.get('LIN03')
		hierarchial_order.SN102 = form.cleaned_data.get('SN102')
		hierarchial_order.SN103 = form.cleaned_data.get('SN103')
		hierarchial_order.SN104 = form.cleaned_data.get('SN104')
		hierarchial_order.PRF01 = form.cleaned_data.get('PRF01')
		hierarchial_order.REF101 = form.cleaned_data.get('REF101')
		hierarchial_order.REF102 = form.cleaned_data.get('REF102')
		hierarchial_order.REF201 = form.cleaned_data.get('REF201')
		hierarchial_order.REF202 = form.cleaned_data.get('REF202')
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
	#measures = Data_Generator_I_MEA()
	form = ASN_Item(request.POST or None)
	#item_cld = Data_Generator_I_CLD()
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
		hierarchial_order.MEA01 = "PD"
		hierarchial_order.MEA02 = form.cleaned_data.get('MEA02')
		hierarchial_order.MEA03 = form.cleaned_data.get('MEA03')
		hierarchial_order.MEA04 = form.cleaned_data.get('MEA04')
		hierarchial_order.MEA201 = "PD"
		hierarchial_order.MEA202 = form.cleaned_data.get('MEA202')
		hierarchial_order.MEA203 = form.cleaned_data.get('MEA203')
		hierarchial_order.MEA204 = form.cleaned_data.get('MEA204')
		hierarchial_order.MEA301 = "PD"
		hierarchial_order.MEA302 = form.cleaned_data.get('MEA302')
		hierarchial_order.MEA303 = form.cleaned_data.get('MEA303')
		hierarchial_order.MEA304 = form.cleaned_data.get('MEA304')
		hierarchial_order.MEA401 = "PD"
		hierarchial_order.MEA402 = form.cleaned_data.get('MEA402')
		hierarchial_order.MEA403 = form.cleaned_data.get('MEA403')
		hierarchial_order.MEA404 = form.cleaned_data.get('MEA404')
		hierarchial_order.CLD01 = form.cleaned_data.get('CLD01')
		hierarchial_order.CLD02 = form.cleaned_data.get('CLD02')
		hierarchial_order.CLD03 = form.cleaned_data.get('CLD03')
		hierarchial_order.REF_CLD101 = form.cleaned_data.get('REF_CLD101')
		hierarchial_order.REF_CLD102 = form.cleaned_data.get('REF_CLD102')
		hierarchial_order.REF_CLD201 = form.cleaned_data.get('REF_CLD201')
		hierarchial_order.REF_CLD202 = form.cleaned_data.get('REF_CLD202')
		hierarchial_order.REF_CLD301 = form.cleaned_data.get('REF_CLD301')
		hierarchial_order.REF_CLD302 = form.cleaned_data.get('REF_CLD302')
		hierarchial_order.REF_CLD401 = form.cleaned_data.get('REF_CLD401')
		hierarchial_order.REF_CLD402 = form.cleaned_data.get('REF_CLD402')
		hierarchial_order.REF_ITEM101 = form.cleaned_data.get('REF_ITEM101')
		hierarchial_order.REF_ITEM102 = form.cleaned_data.get('REF_ITEM102')
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
	#measures = Data_Generator_I_MEA.objects.filter(PRIM_id=master_id)
	return render(request, 'EDI/render/edi.html', {'edi':edi, 'hl':hl, 'order':order,})



