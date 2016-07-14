from django.contrib import admin
from .models import edi_address
# Register your models here.

class edi_address_admin(admin.ModelAdmin):
	list_display = ['edi_name']
	search_fields = ['edi_name']
admin.site.register (edi_address, edi_address_admin)