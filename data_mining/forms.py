from django import forms
from models import edi_address
class DocumentForm(forms.ModelForm):
    docfile = forms.FileField()
    class Meta:
    	model = edi_address
    	fields = ["docfile",]
