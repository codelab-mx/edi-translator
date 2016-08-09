# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Company_Data(models.Model):
	C_Prefix = models.CharField(max_length = 5)
	C_Name = models.CharField(max_length = 100)
	C_Address = models.CharField(max_length = 50)

class Partner_Data(models.Model):
	P_Prefix = models.CharField(max_length = 5)
	P_Name = models.CharField(max_length = 100)
	DUNS = models.CharField(max_length = 50)
	P_Address = models.CharField(max_length = 50)
	E_mail	= models.CharField(max_length = 100)
	
	

