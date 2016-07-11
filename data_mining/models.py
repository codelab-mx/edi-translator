from __future__ import unicode_literals

from django.db import models


class data_segments(models.Model):

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
	ST_3 = models.CharField(blank = True, max_length = 50)

