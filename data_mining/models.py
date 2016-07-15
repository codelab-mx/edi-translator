from __future__ import unicode_literals
from django.db import models
from validators import file_size
import os

class edi_address(models.Model):
	#edi_name = models.CharField(max_length= 50)
	edi_file = models.FileField(upload_to='edi/', validators=[file_size])
	def filename(self):
		return os.path.basename(self.edi_file.name)


class data_segments_master(models.Model):
	edi = models.ForeignKey(edi_address, on_delete= models.CASCADE)
	GS_1 = models.CharField(blank = True, max_length = 50)
	GS_2 = models.CharField(blank = True, max_length = 50)
	GS_3 = models.CharField(blank = True, max_length = 50)
	GS_4 = models.CharField(blank = True, max_length = 50)
	GS_5 = models.CharField(blank = True, max_length = 50)
	GS_6 = models.CharField(blank = True, max_length = 50)
	GS_7 = models.CharField(blank = True, max_length = 50)
	GS_8 = models.CharField(blank = True, max_length = 50)
	ST_1 = models.CharField(blank = True, max_length = 50)
	ST_2 = models.CharField(blank = True, max_length = 50)
	UIT_1 = models.CharField(blank = True, max_length = 50)
	UIT_2 = models.CharField(blank = True, max_length = 50)
	UIT_3 = models.CharField(blank = True, max_length = 50)
	SHP_1 = models.CharField(blank = True, max_length = 50)
	SHP_2 = models.CharField(blank = True, max_length = 50)
	SHP_3 = models.CharField(blank = True, max_length = 50)
	SHP_4 = models.CharField(blank = True, max_length = 50)
	SHP_5 = models.CharField(blank = True, max_length = 50)
	SHP_6 = models.CharField(blank = True, max_length = 50)
	SHP_7 = models.CharField(blank = True, max_length = 50)
	CT_1 = 	models.CharField(blank = True, max_length = 50)
	CT_2 = models.CharField(blank = True, max_length = 50)
	SE_1 = 	models.CharField(blank = True, max_length = 50)
	SE_2 = models.CharField(blank = True, max_length = 50)
	GE_1 = models.CharField(blank = True, max_length = 50)
	GE_2 = models.CharField(blank = True, max_length = 50)
	IEA_1 = models.CharField(blank = True, max_length = 50)
	IEA_2 = models.CharField(blank = True, max_length = 50)


class data_segments_BFR(models.Model):
	BFR_1 = models.CharField(blank = True, max_length = 50)
	BFR_2 = models.CharField(blank = True, max_length = 50)
	BFR_3 = models.CharField(blank = True, max_length = 50)
	BFR_4 = models.CharField(blank = True, max_length = 50)
	BFR_5 = models.CharField(blank = True, max_length = 50)
	BFR_6 = models.CharField(blank = True, max_length = 50)
	BFR_7 = models.CharField(blank = True, max_length = 50)
	BFR_8 = models.CharField(blank = True, max_length = 50)
	BFR_11 = models.CharField(blank = True, max_length = 50)

class data_segments_N(models.Model):
	prim = models.ForeignKey(data_segments_master, on_delete= models.CASCADE)
	N_0 = models.CharField(blank = True, max_length = 50)
	N_1 = models.CharField(blank = True, max_length = 50)
	N_2 = models.CharField(blank = True, max_length = 50)
	N_3 = models.CharField(blank = True, max_length = 50)
	N_4 = models.CharField(blank = True, max_length = 50)

class data_segments_830LIN(models.Model):
	LIN_1 = models.CharField(blank = True, max_length = 50)
	LIN_2 = models.CharField(blank = True, max_length = 50)
	LIN_3 = models.CharField(blank = True, max_length = 50)
	LIN_4 = models.CharField(blank = True, max_length = 50)
	LIN_5 = models.CharField(blank = True, max_length = 50)
	LIN_6 = models.CharField(blank = True, max_length = 50)
	LIN_7 = models.CharField(blank = True, max_length = 50)
	LIN_8 = models.CharField(blank = True, max_length = 50)
	LIN_9 = models.CharField(blank = True, max_length = 50)
	LIN_10 = models.CharField(blank = True, max_length = 50)
	LIN_11 = models.CharField(blank = True, max_length = 50)
	LIN_12 = models.CharField(blank = True, max_length = 50)
	LIN_13 = models.CharField(blank = True, max_length = 50)
	LIN_14 = models.CharField(blank = True, max_length = 50)
	LIN_15 = models.CharField(blank = True, max_length = 50)

class data_segments_FST(models.Model):
	prim = models.ForeignKey(data_segments_master, on_delete= models.CASCADE, null = True)
	FST_0 = models.CharField(blank = True, max_length = 50)
	FST_1 = models.CharField(blank = True, max_length = 50)
	FST_2 = models.CharField(blank = True, max_length = 50)
	FST_3 = models.CharField(blank = True, max_length = 50)
	FST_4 = models.CharField(blank = True, max_length = 50)
	FST_5 = models.CharField(blank = True, max_length = 50)
	FST_6 = models.CharField(blank = True, max_length = 50)
	FST_7 = models.CharField(blank = True, max_length = 50)
	FST_8 = models.CharField(blank = True, max_length = 50)
	FST_9 = models.CharField(blank = True, max_length = 50)
	FST_10 = models.CharField(blank = True, max_length = 50)