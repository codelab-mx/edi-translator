# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Company_Data(models.Model):
	C_Name = models.CharField(max_length = 100)
	C_Edi_Address = models.CharField(max_length = 50)
	C_Country = models.CharField(blank = True, max_length = 100)
	C_City = models.CharField(blank = True, max_length = 100)
	C_ZIP = models.CharField(blank = True, max_length = 100)
	C_E_mail = models.CharField(blank = True, max_length = 100)
	C_Phone = models.CharField(blank = True, max_length = 100)
	C_Address = models.CharField(blank = True, max_length = 100)

class Partner_Data(models.Model):
	P_Name = models.CharField(max_length = 100)
	P_Edi_Address = models.CharField(max_length = 50)
	P_Country = models.CharField(blank = True, max_length = 100)
	P_City = models.CharField(blank = True, max_length = 100)
	P_ZIP = models.CharField(blank = True, max_length = 100)
	P_E_mail = models.CharField(blank = True, max_length = 100)
	P_Phone = models.CharField(blank = True, max_length = 100)
	P_Address = models.CharField(blank = True, max_length = 100)
	

