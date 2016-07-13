import glob
import errno
import os
import sys
from django.db import connection 
sys.path.append('/home/zardain/Documents/Proyectos/edi-translator/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from data_mining.models import data_segments_master, data_segments_BFR, data_segments_N, data_segments_830LIN, data_segments_FST

def get_file_address():
	global path, files
	path = '/home/zardain/Documents/Proyectos/edi-translator/media/28057'   
	files = glob.glob(path)
	model_ini()

def read_file():
	#print "reading file"
	global path, files, lines, cont
	lines = []
	for name in files:
		with open(name) as f:
			for line in f:
				lines.append(line.rstrip('\n'))
		num_lineas = len(lines)
		while (cont < num_lineas):
			segment_lines()
			cont = cont + 1
			#print cont
	return

def segment_lines():
	#print "segment line"
	global lines, cont, segment_text, flag, name
	texto = str(lines[cont])
	segment_text = texto.split("*")
	if segment_text[1] == "PS":
		flag = True
	if flag == True:
		flow_830()


def flow_830():
	#print "determing EDI type"
	global cont, name, cont_FST
	if segment_text[0] == "sjbfvjsd":
		print "hi"

	else:

		lista = {'GS':GS,
			 	'ST':ST,
			 	'BFR':BFR,
			 	'N1':N,
			 	'LIN':LIN,
			 	'UIT':UIT,
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
	return

def model_ini():
	global model_master, model_BFR, model_830LIN
	model_master = data_segments_master()
	model_BFR = data_segments_BFR()
	model_830LIN = data_segments_830LIN()
	read_file()

def model_save():
	global model
	model.save()


#############################
#  FUNCTIONAL GROUP HEADER  #
#############################

def GS():
	global segment_text, model_master, primary_key
	model_master.GS_1 = segment_text[1]
	model_master.GS_2 = segment_text[2]
	model_master.GS_3 = segment_text[3]
	model_master.GS_4 = segment_text[4]
	model_master.GS_5 = segment_text[5]
	model_master.GS_6 = segment_text[6]
	model_master.GS_7 = segment_text[7]
	model_master.GS_8 = segment_text[8]
	primary_key = segment_text[6]
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


#######################
#  Beginning Segment  #
#######################

def BFR():
	global segment_text, model_BFR
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
		model_BFR.save()
	return

##################
#  Name Segment  #
##################


def N():
	global segment_text, primary_key
	model_N1 = data_segments_N()
	primary = data_segments_master.objects.get(GS_6=primary_key)
	model_N1.prim = primary
	model_N1.N_0 = segment_text[0]
	model_N1.N_1 = segment_text[1]
	model_N1.N_2 = segment_text[2]
	model_N1.N_3 = segment_text[3]
	model_N1.N_4 = segment_text[4]
	model_N1.save()
	return



def FST():
	global segment_text, primary_key
	model_FST = data_segments_FST()
	primary = data_segments_master.objects.get(GS_6=primary_key)
	model_FST.prim = primary
	model_FST.FST_0 = segment_text[0]
	model_FST.FST_1 = segment_text[1]
	model_FST.FST_2 = segment_text[2]
	model_FST.FST_3 = segment_text[3]
	model_FST.FST_4 = segment_text[4]
	#model_FST.FST_5 = segment_text[5]
	#model_FST.FST_6 = segment_text[6]
	#model_FST.FST_7 = segment_text[7]
	#model_FST.FST_8 = segment_text[8]
	#model_FST.FST_9 = segment_text[9]
	#model_FST.FST_10 = segment_text[10]
	model_FST.save()
	return



def LIN():
	global model_830LIN
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
	model_830LIN.save()
	return

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

def SHP():
	global model_master
	try:
		model_master.SHP_1 = segment_text[1]
		model_master.SHP_2 = segment_text[2]
		model_master.SHP_3 = segment_text[3]
		model_master.SHP_4 = segment_text[4]
		model_master.SHP_4 = segment_text[5]
		model_master.SHP_4 = segment_text[6]
		model_master.SHP_4 = segment_text[7]
		model_master.save()
	except:
		model_master.SHP_1 = segment_text[1]
		model_master.SHP_2 = segment_text[2]
		model_master.SHP_3 = segment_text[3]
		model_master.SHP_4 = segment_text[4]
		model_master.save()
	return

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


if __name__ == '__main__':
	global flag, name, cont, cont_FST
	cont = 1
	flag = False
	name = 0
	cont_FST = 0
	get_file_address()