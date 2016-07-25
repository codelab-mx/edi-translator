# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Data_Generator_Master(models.Model):
	NAME = models.CharField(max_length = 50)
	ST01 = models.CharField(max_length = 50)
	ST02 = models.CharField(max_length = 50)
	BST01 = models.CharField(max_length = 50)
	BST02 = models.CharField(max_length = 50)
	BST03 = models.CharField(max_length = 50)
	BST04 = models.CharField(max_length = 50)
	DTM01 = models.CharField(max_length = 50)
	DTM02 = models.CharField(max_length = 50)
	DTM03 = models.CharField(max_length = 50)
	DTM04 = models.CharField(max_length = 50)
	DTM05 = models.CharField(max_length = 50)
	MEA01 = models.CharField(max_length = 50)
	MEA02 = models.CharField(max_length = 50)
	MEA03 = models.CharField(max_length = 50)
	MEA04 = models.CharField(max_length = 50)
	TD101 = models.CharField(max_length = 50)
	TD102 = models.CharField(max_length = 50)
	TD501 = models.CharField(max_length = 50)
	TD502 = models.CharField(max_length = 50)
	TD503 = models.CharField(max_length = 50)
	TD504 = models.CharField(max_length = 50)
	TD505 = models.CharField(blank = True, max_length = 50)
	TD506 = models.CharField(blank = True, max_length = 50)
	TD507 = models.CharField(blank = True, max_length = 50)
	TD508 = models.CharField(blank = True, max_length = 50)
	TD301 = models.CharField(max_length = 50)
	TD302 = models.CharField(blank = True, max_length = 50)
	TD303 = models.CharField(max_length = 50)
	TD401 = models.CharField(max_length = 50)
	TD402 = models.CharField(max_length = 50)
	TD403 = models.CharField(max_length = 50)
	TD404 = models.CharField(blank = True, max_length = 50)
	TD405 = models.CharField(blank = True, max_length = 50)
	REF01 = models.CharField(max_length = 50)
	REF02 = models.CharField(max_length = 50)
	LIN01 = models.CharField(blank = True, max_length = 50)
	LIN02 = models.CharField(max_length = 50)
	LIN03 = models.CharField(max_length = 50)
	SN101 = models.CharField(blank = True, max_length = 50)
	SN102 = models.CharField(max_length = 50)
	SN103 = models.CharField(max_length = 50)
	SN104 = models.CharField(max_length = 50)
	CLD01 = models.CharField(max_length = 50)
	CLD02 = models.CharField(max_length = 50)
	CLD03 = models.CharField(max_length = 50)
	ETD01 = models.CharField(max_length = 50)
	ETD02 = models.CharField(max_length = 50)
	ETD03 = models.CharField(max_length = 50)
	CTT01 = models.CharField(max_length = 50)
	CTT02 = models.CharField(max_length = 50)
	SE01 = models.CharField(max_length = 50)
	SE02 = models.CharField(max_length = 50)



class Data_Generator_Hierarchial(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	HL01 = models.CharField(max_length = 50)
	HL02 = models.CharField(max_length = 50)
	HL03 = models.CharField(max_length = 50)

class Data_Generator_Name(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	N101 = models.CharField(max_length = 50)
	N102 = models.CharField(blank = True, max_length = 50)
	N103 = models.CharField(max_length = 50)
	N104 = models.CharField(max_length = 50)

class Data_Generator_O_REF(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	REF01 = models.CharField(blank = True, max_length = 50)
	REF02 = models.CharField(blank = True, max_length = 50)

class Data_Generator_I_MEA(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	MEA01 = models.CharField(max_length = 50)
	MEA02 = models.CharField(max_length = 50)
	MEA03 = models.CharField(max_length = 50)
	MEA04 = models.CharField(max_length = 50)

class Data_Generator_I_REF(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	REF01 = models.CharField(blank = True, max_length = 50)
	REF02 = models.CharField(blank = True, max_length = 50)

class Data_Generator_REF(models.Model):
	PRIM = models.ForeignKey(Data_Generator_Master, on_delete= models.CASCADE)
	REF01 = models.CharField(max_length = 50)
	REF02 = models.CharField(max_length = 50)
