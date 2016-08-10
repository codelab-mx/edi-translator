# -*- coding: utf-8 
"""
Empresa: Codelab
Proyecto: Edi-Transalator
Author: Gonzalo Zardain
Fecha: 14 de Julio de 2016

Reseña: data.py lee los datos de un archivo edi que tiene informacion bajo la norma MAGNA 830 y 862
Los guarda en una base de datos para despues poder ser comparada.

"""
import glob, errno, os, sys, django

###########################
# Configuracion de django #
###########################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

###############################
# Importar los modelos a usar #
###############################
from data_mining.models import data_segments_master, data_segments_BFR, data_segments_N, data_segments_830LIN, data_segments_FST, data_segments_BSS, data_segments_862LIN, data_segments_ATH, data_segments_SHP
from models import edi_address
###########################################
# Obtiene la direccion del archivo a leer #
###########################################
def get_file_address():
	global path, files, id_edi, address
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(BASE_DIR, "media/{}".format(address))
	files = glob.glob(path)
	model_ini()

#################################
# Segmenta el archivo por linea #
#################################
def read_file():
	global path, files, lines, cont, model_edi, id_edi
	lines = []
	for name in files:
		with open(name) as f:
			for line in f:
				lines.append(line.rstrip('\n'))
		num_lineas = len(lines)
		while (cont < num_lineas):
			segment_lines()
			cont = cont + 1
	edi_address.objects.filter(id=id_edi).update(flag=True)
	return
#############################################
# segmenta las lineas por palabras filtra * #
#############################################
def segment_lines():
	global lines, cont, segment_text, flag, name
	texto = str(lines[cont])
	segment_text = texto.split("*")
	

	if segment_text[1] == "PS":
		flag = True
	if flag == True:
		flow_830()
	elif segment_text[1] == "SS":
		flag = False
	if flag == False:
		flow_862()


#############################
# Flujo para un archivo 862 #
#############################
def flow_862():
	global cont, name, cont_FST

	try:
		lista = {'GS':GS,
				 'ST':ST,
				 'BSS':BSS,
				 'DTM':DTM,
				 'N1':N,
				 'PER':PER,
				 'LIN':LIN_862,
				 'UIT':UIT,
				 'FST':FST,
				 'SHP':SHP,
				 'REF':REF,
				 'CTT':CTT,
				 'SE':SE,
				 'GE':GE,
				 'IEA':IEA, 
				}
		strcont = segment_text[0]
		trigger = lista[strcont]
		trigger()
	except:
		do_nothing()
	return

		

#############################
# Flujo para un archivo 830 #
#############################
def flow_830():
	global cont, name, cont_FST

	try:

		lista = {'GS':GS,
				 'ST':ST,
				 'BFR':BFR,
				 'DTM':DTM,
				 'N1':N,
				 'N3':N3,
				 'N4':N4,
				 'PER':PER,
				 'LIN':LIN_830,
				 'PID':PID,
				 'UIT':UIT,
				 'REF':REF,
				 'PER':PER,
				 'ATH':ATH,
				 'SDP':SDP,
				 'FST':FST,
				 'SHP':SHP,
				 'CTT':CTT,
				 'SE':SE,
				 'GE':GE,
				 'IEA':IEA, 
				}
		strcont = segment_text[0]
		trigger = lista[strcont]
		trigger()
	except:
		do_nothing()
	return

def do_nothing():
	return

##########################################
# inicializacion de los modelos globales #
##########################################
def model_ini():
	global model_master, model_BFR, model_830LIN, model_BSS, model_862LIN, model_ATH
	model_master = data_segments_master()
	model_BFR = data_segments_BFR()
	model_BSS = data_segments_BSS()
	model_830LIN = data_segments_830LIN()
	model_862LIN = data_segments_862LIN()
	model_ATH = data_segments_ATH()
	read_file()

#############################
#  FUNCTIONAL GROUP HEADER  #
#############################
def GS():
	global segment_text, model_master, primary_key, id_edi
	model_master.GS_1 = segment_text[1]
	model_master.GS_2 = segment_text[2]
	model_master.GS_3 = segment_text[3]
	model_master.GS_4 = segment_text[4]
	model_master.GS_5 = segment_text[5]
	model_master.GS_6 = segment_text[6]
	model_master.GS_7 = segment_text[7]
	model_master.GS_8 = segment_text[8]
	model_master.edi = edi_address.objects.get(id = id_edi)
	model_master.id = id_edi
	model_master.save()
	return

#############################
#  TRANSACTION SET HEADER   #
#############################
def ST():
	global segment_text, model_1
	model_master.ST_1 = segment_text[1]
	model_master.ST_2 = segment_text[2]
	model_master.save()
	return

##########################
#  DATE TIME REFERENCE   #
##########################
def DTM():
	global segment_text, model_1
	model_master.DTM_1 = segment_text[1]
	model_master.DTM_2 = segment_text[2]
	model_master.DTM_3 = segment_text[3]
	model_master.save()
	return

############################
#  SHIP/DELIVERY PATTERN   #
############################
def SDP():
	global segment_text, model_1
	model_master.SPD_1 = segment_text[1]
	model_master.SPD_2 = segment_text[2]
	model_master.save()
	return

#######################
#  REFERENCE NUMBERS  #
#######################

def REF():
	global segment_text, model_1
	model_master.REF_1 = segment_text[1]
	model_master.REF_2 = segment_text[2]
	model_master.save()
	return

########################
#  ADMINISTRATIVE COM  #
########################

def PER():
	global segment_text, model_1
	model_master.PER_1 = segment_text[1]
	model_master.PER_2 = segment_text[2]
	model_master.PER_3 = segment_text[3]
	model_master.PER_4 = segment_text[4]
	model_master.save()
	return


#######################
#  Beginning Segment  #
#######################
def BSS():
	global segment_text, model_BSS, id_edi
	try:
		model_BSS.BSS_1 = segment_text[1]
		model_BSS.BSS_2 = segment_text[2]
		model_BSS.BSS_3 = segment_text[3]
		model_BSS.BSS_4 = segment_text[4]
		model_BSS.BSS_5 = segment_text[5]
		model_BSS.BSS_6 = segment_text[6]
		model_BSS.BSS_7 = segment_text[7]
		model_BSS.BSS_8 = segment_text[8]
		model_BSS.BSS_11 = segment_text[11]
		model_BSS.prim = data_segments_master.objects.get(id=id_edi)
		model_BSS.save()

	except:
		model_BSS.BSS_1 = segment_text[1]
		model_BSS.BSS_2 = segment_text[2]
		model_BSS.BSS_3 = segment_text[3]
		model_BSS.BSS_4 = segment_text[4]
		model_BSS.BSS_5 = segment_text[5]
		model_BSS.BSS_6 = segment_text[6]
		model_BSS.BSS_7 = segment_text[7]
		model_BSS.BSS_8 = segment_text[8]
		model_BSS.prim = data_segments_master.objects.get(id=id_edi)
		model_BSS.save()
	return

#######################
#  Beginning Segment  #
#######################
def BFR():
	global segment_text, model_BFR, id_edi
	try:
		model_BFR.BFR_1 = segment_text[1]
		model_BFR.BFR_2 = segment_text[2]
		model_BFR.BFR_3 = segment_text[3]
		model_BFR.BFR_4 = segment_text[4]
		model_BFR.BFR_5 = segment_text[5]
		model_BFR.BFR_6 = segment_text[6]
		model_BFR.BFR_7 = segment_text[7]
		model_BFR.BFR_8 = segment_text[8]
		model_BFR.BFR_11 = segment_text[11]
		model_BFR.prim = data_segments_master.objects.get(id=id_edi)
		model_BFR.save()

	except:
		model_BFR.BFR_1 = segment_text[1]
		model_BFR.BFR_2 = segment_text[2]
		model_BFR.BFR_3 = segment_text[3]
		model_BFR.BFR_4 = segment_text[4]
		model_BFR.BFR_5 = segment_text[5]
		model_BFR.BFR_6 = segment_text[6]
		model_BFR.BFR_7 = segment_text[7]
		model_BFR.BFR_8 = segment_text[8]
		model_BFR.prim = data_segments_master.objects.get(id=id_edi)
		model_BFR.save()
	return


##################
#  Name Segment  #
##################
def N():
	global segment_text, primary_key, id_edi
	model_N1 = data_segments_N()
	primary = data_segments_master.objects.get(id=id_edi)
	model_N1.prim = primary
	model_N1.N_0 = segment_text[0]
	model_N1.N_1 = segment_text[1]
	model_N1.N_2 = segment_text[2]
	model_N1.N_3 = segment_text[3]
	model_N1.N_4 = segment_text[4]
	model_N1.save()
	return

##################
#  Name3 Segment  #
##################
def N3():
	global segment_text, primary_key, id_edi
	#model_N1 = data_segments_N()
	#primary = data_segments_master.objects.get(id=id_edi)
	#model_N1.N3_0 = segment_text[0]
	#model_N1.N3_1 = segment_text[1]
	#model_N1.save()
	return

##################
#  Name4 Segment  #
##################
def N4():
	global segment_text, primary_key, id_edi
	#model_N1 = data_segments_N()
	#primary = data_segments_master.objects.get(id=id_edi)
	#model_N1.N4_0 = segment_text[0]
	#model_N1.N4_1 = segment_text[1]
	#model_N1.N4_2 = segment_text[2]
	#model_N1.N4_3 = segment_text[3]
	#model_N1.save()
	return

############################
#  Resource Authorization  #
############################

def ATH():
	global segment_text, primary_key, id_edi
	model_ATH = data_segments_ATH()
	primary = data_segments_master.objects.get(id=id_edi)
	model_ATH.prim = primary
	model_ATH.ATH_0 = segment_text[0]
	model_ATH.ATH_1 = segment_text[1]
	model_ATH.ATH_2 = segment_text[2]
	model_ATH.ATH_3 = segment_text[3]
	model_ATH.ATH_4 = segment_text[4]
	model_ATH.ATH_5 = segment_text[5]
	model_ATH.save()
	return

#####################
# Forecast Schedule #
#####################
def FST():
	global segment_text, primary_key, id_edi, RLIN_3, RLIN_15
	model_FST = data_segments_FST()
	primary = data_segments_master.objects.get(id=id_edi)
	model_FST.prim = primary
	model_FST.FST_0 = segment_text[0]
	model_FST.FST_1 = segment_text[1]
	model_FST.FST_2 = segment_text[2]
	model_FST.FST_3 = segment_text[3]
	model_FST.FST_4 = segment_text[4]
	model_FST.FST_5 = RLIN_3
	model_FST.FST_6 = RLIN_15
	#model_FST.FST_7 = segment_text[7]
	#model_FST.FST_8 = segment_text[8]
	#model_FST.FST_9 = segment_text[9]
	#model_FST.FST_10 = segment_text[10]
	model_FST.save()
	return

#######################
# Item Identification #
#######################
def LIN_830():
	global  id_edi, RLIN_3, RLIN_15
	model_830LIN = data_segments_830LIN()
	try:

		model_830LIN.LIN_1 = segment_text[1]
		model_830LIN.LIN_2 = segment_text[2]
		model_830LIN.LIN_3 = segment_text[3]
		model_830LIN.LIN_4 = segment_text[4]
		model_830LIN.LIN_5 = segment_text[5]
		model_830LIN.LIN_6 = segment_text[6]
		model_830LIN.LIN_7 = segment_text[7]
		model_830LIN.LIN_8 = segment_text[8]
		model_830LIN.LIN_9 = segment_text[9]
		model_830LIN.LIN_10 = segment_text[10]
		model_830LIN.LIN_11= segment_text[11]
		model_830LIN.LIN_12= segment_text[12]
		model_830LIN.LIN_13= segment_text[13]
		model_830LIN.LIN_14= segment_text[14]
		model_830LIN.LIN_15= segment_text[15]
		RLIN_3 = segment_text[3]
		RLIN_15 = segment_text[15]
		model_830LIN.prim = data_segments_master.objects.get(id=id_edi)
		model_830LIN.save()
	except:
		model_830LIN.LIN_1 = segment_text[1]
		model_830LIN.LIN_2 = segment_text[2]
		model_830LIN.LIN_3 = segment_text[3]
		model_830LIN.LIN_4 = segment_text[4]
		model_830LIN.LIN_5 = segment_text[5]
		model_830LIN.LIN_6 = segment_text[6]
		model_830LIN.LIN_7 = segment_text[7]
		RLIN_3 = segment_text[3]
		model_830LIN.prim = data_segments_master.objects.get(id=id_edi)
		model_830LIN.save()

	return

#######################
# Item Identification #
#######################
def LIN_862():
	global model_862LIN, id_edi, RLIN_3, RLIN_15
	model_862LIN.LIN_1 = segment_text[1]
	model_862LIN.LIN_2 = segment_text[2]
	model_862LIN.LIN_3 = segment_text[3]
	model_862LIN.LIN_4 = segment_text[4]
	model_862LIN.LIN_5 = segment_text[5]
	model_862LIN.LIN_6 = segment_text[6]
	model_862LIN.LIN_7 = segment_text[7]
	#model_862LIN.LIN_8 = segment_text[8]
	#model_862LIN.LIN_9 = segment_text[9]
	#model_862LIN.LIN_10 = segment_text[10]
	#model_862LIN.LIN_11= segment_text[11]
	#model_862LIN.LIN_12= segment_text[12]
	#model_862LIN.LIN_13= segment_text[13]
	#model_862LIN.LIN_14= segment_text[14]
	#model_862LIN.LIN_15= segment_text[15]
	RLIN_3 = segment_text[3]
	RLIN_15 = ""
	model_862LIN.prim = data_segments_master.objects.get(id=id_edi)
	model_862LIN.save()
	return



#############################
#  TRANSACTION SET HEADER   #
#############################
def PID():
	global segment_text, model_1, RLIN_15
	RLIN_15 = segment_text[5]
	return

###############
# Unit Detail #
###############
def UIT():
	try:
		model_master.UIT_1 = segment_text[1]
		model_master.UIT_2 = segment_text[2]
		model_master.UIT_3 = segment_text[3]
		model_master.save()
	except:
		model_master.UIT_1 = segment_text[1]
		model_master.save()
	return

################################
# Shipped/Received Information #
################################
def SHP():
	global id_edi
	model_SHP = data_segments_SHP()
	primary = data_segments_master.objects.get(id=id_edi)
	try:
		model_SHP.prim = data_segments_master.objects.get(id=id_edi)
		model_SHP.SHP_1 = segment_text[1]
		model_SHP.SHP_2 = segment_text[2]
		model_SHP.SHP_3 = segment_text[3]
		model_SHP.SHP_4 = segment_text[4]
		model_SHP.SHP_5 = segment_text[5]
		model_SHP.SHP_6 = segment_text[6]
		model_SHP.SHP_7 = segment_text[7]
		model_SHP.save()
	except:
		model_SHP.prim = data_segments_master.objects.get(id=id_edi)
		model_SHP.SHP_1 = segment_text[1]
		model_SHP.SHP_2 = segment_text[2]
		model_SHP.SHP_3 = segment_text[3]
		model_SHP.SHP_4 = segment_text[4]
		model_SHP.save()
	return

#######################
# Transaction Totals  #
#######################
def CTT():
	global model_master
	try:
		model_master.CT_1 = segment_text[1]
		model_master.CT_2 = segment_text[2]
		model_master.save()
	except:
		model_master.CT_1 = segment_text[1]
		model_master.save()
	return

###########################
# Transaction Set Trailer #
###########################
def SE():
	global model_master
	model_master.SE_1 = segment_text[1]
	model_master.SE_2 = segment_text[2]
	model_master.save()
	return

def GE():
	global model_master
	model_master.GE_1 = segment_text[1]
	model_master.GE_2 = segment_text[2]
	model_master.save()
	return 

def IEA():
	global model_master
	model_master.IEA_1 = segment_text[1]
	model_master.IEA_2 = segment_text[2]
	model_master.save()
	return

def PER():
	return

def init_data(id_edi_local, address_local, flag_local):
	global flag, name, cont, cont_FST, id_edi, address, flag
	cont = 1
	flag = False
	name = 0
	cont_FST = 0
	id_edi = id_edi_local
	address = str(address_local)
	flag = flag_local
	get_file_address()

if __name__ == '__main__':
	global flag, name, cont, cont_FST
	cont = 1
	flag = False
	name = 0
	cont_FST = 0
	get_file_address()