#aqui van las formas chingonas
from django import forms
from models import Data_Generator_Master, Data_Generator_Order
from django.core.validators import RegexValidator

class ASN_Heading(forms.ModelForm):
	ST01 = forms.CharField(widget=forms.HiddenInput(), initial="856")
	BST02 = forms.CharField(widget=forms.HiddenInput(), initial="00")
	ST02 = forms.CharField(label='Transaction Control Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST01 = forms.CharField(label='Purpose Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST03 = forms.CharField(label='Date', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST04 = forms.CharField(label='Time', widget=forms.TextInput(attrs={'class': 'form-control'}))
	DTM01 = forms.CharField(widget=forms.HiddenInput(), initial="011")
	DTM02 = forms.CharField(widget=forms.HiddenInput(), initial="0")
	DTM03 = forms.CharField(widget=forms.HiddenInput(), initial="0")
	DTM04 = forms.CharField(label='Time Zone', widget=forms.TextInput(attrs={'placeholder': 'Use Mexico Central', 'class': 'form-control'}))
	DTM05 = forms.CharField(widget=forms.HiddenInput(), initial="21")

	class Meta:
		model = Data_Generator_Master
		fields = ["ST02", "BST01", "BST03", "BST04", "DTM04", "ST01"]

class ASN_Shipment(forms.ModelForm):
	HL01 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	HL02 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	HL03 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	MEA01 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	MEA02 = forms.CharField(label='Weight Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA03 = forms.CharField(label='Weight Value', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA04 = forms.CharField(label='Weight Unit', widget=forms.TextInput(attrs={'placeholder': 'KG MM L LBS .. ETC', 'class': 'form-control'}))
	TD101 = forms.CharField(label='Packaging Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD102 = forms.CharField(label='Landing Quantity', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD501 = forms.CharField(widget=forms.HiddenInput(), initial="B")
	TD502 = forms.CharField(widget=forms.HiddenInput(), initial="2")
	TD503 = forms.CharField(label='ID Code', widget=forms.TextInput(attrs={'placeholder': 'Code Identifying a Party','class': 'form-control'}))
	TD504 = forms.CharField(label='Transportation Method', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD507 = forms.CharField(label='Location Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD508 = forms.CharField(label='Location ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD301 = forms.CharField(label='Equipment Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD302 = forms.CharField(label='Equipment Initial', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD303 = forms.CharField(label='Equipment Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD401 = forms.CharField(required=False, label='Special Handling Code', widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}))
	TD402 = forms.CharField(required=False, label='Hazardous Qualifier', widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}))
	TD403 = forms.CharField(required=False, label='Hazardous Code', widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}))
	TD404 = forms.CharField(required=False, label='Description', widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}))
	TD405 = forms.CharField(required=False, label='Condition', widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class': 'form-control'}))
	REF01 = forms.CharField(label='Reference Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF02 = forms.CharField(label='Reference ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Master
		fields = ["MEA02", "MEA03", "MEA04", "TD101", "TD102", "TD503", "TD504", "TD507", "TD508", "TD301", "TD302", "TD303", "TD401", "TD402", "TD403", "TD404", "TD405", "REF01", "REF02"]


class ASN_Order(forms.ModelForm):
	HL01 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	HL02 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	HL03 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	LIN02 = forms.CharField(label='Product Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	LIN03 = forms.CharField(label='Product ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SN102 = forms.CharField(label='Number of Units Shiped', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SN103 = forms.CharField(label='Unit', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SN104 = forms.CharField(label='Quantity Shipped', widget=forms.TextInput(attrs={'class': 'form-control'}))
	PRF01 = forms.CharField(label='Purchase Order Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Order
		fields = ["LIN02", "LIN03", "SN102", "SN103", "SN104", "PRF01"]