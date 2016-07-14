from django.contrib import admin
from .models import edi_address
# Register your models here.

class edi_address_admin(admin.ModelAdmin):
	list_display = ['id']
	search_fields = ['id']

admin.site.register (edi_address, edi_address_admin)