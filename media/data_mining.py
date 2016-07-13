import glob
import errno
import os
import sys
sys.path.append('/home/zardain/Documents/Proyectos/edi-translator/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
#model_ini()
from data_mining.models import Modelo_GS
print"1"




def get_file_address():
	global path, files
	path = '/home/zardain/Documents/Proyectos/edi-translator/media/26743'   
	files = glob.glob(path)
	read_file()


def read_file():
	#print "reading file"
	global path, files, lines, cont
	lines = []
	for name in files:
		with open(name) as f:
			for line in f:
				lines.append(line.rstrip('\n'))
		num_lineas = len(lines)
		cont = 1
		while (cont < 3):
			segment_lines()
			cont = cont + 1

def segment_lines():
	#print "segment line"
	global lines, cont, segment_text, flag
	texto = str(lines[cont])
	segment_text = texto.split("*")
	if segment_text[1] == "PS":
		flag = True
	if flag == True:
		flow_830()


def flow_830():
	#print "determing EDI type"
	global cont
	lista = {'1':GS,
			 '2':ST,
			 
			}
	strcont = str(cont)
	trigger = lista[strcont]
	trigger()

def model_ini():
	global model
	model = Modelo()

def model_save():
	global model
	model.save()


#############################
#  FUNCTIONAL GROUP HEADER  #
#############################

def GS():
	# global segment_text, model 
	# model.GS_1 = segment_text[1]
	# model.GS_2 = segment_text[2]
	# model.GS_3 = segment_text[3]
	# model.GS_4 = segment_text[4]
	# model.GS_5 = segment_text[5]
	# model.GS_6 = segment_text[6]
	# model.GS_7 = segment_text[7]
	# model.GS_8 = segment_text[8]
	# model_save()
	return

#############################
#  TRANSACTION SET HEADER   #
#############################

def ST():
	global segment_text
	num_posiciones = 1
	while (num_posiciones < len(segment_text)):
		print segment_text[num_posiciones]
		num_posiciones = num_posiciones + 1

if __name__ == '__main__':
	global flag
	flag = False
	print "2"
	get_file_address()