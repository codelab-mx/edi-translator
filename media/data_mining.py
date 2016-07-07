import sys
import glob
import errno

def get_file_address():
	global path, files
	path = '/home/zardain/Documents/Proyectos/edi-translator/media/26743'   
	files = glob.glob(path)
	read_file()


def read_file():
	global path, files, lines, cont
	lines = []
	for name in files:
		with open(name) as f:
			for line in f:
				lines.append(line)
		num_lineas = len(lines)
		cont = 0
		while (cont < num_lineas):
			segment_lines()
			cont = cont + 1

def segment_lines():
	global lines, cont
	texto = str(lines[cont])
	texto_2 = texto.split("*")
	print texto_2



if __name__ == '__main__':
    get_file_address()