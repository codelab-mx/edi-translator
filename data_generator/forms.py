from django import forms
from models import Data_Generator_Master, Data_Generator_Order, Data_Generator_Hierarchial, Data_Generator_Loads
from django.core.validators import RegexValidator

class ASN_Heading(forms.ModelForm):
	ST01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="856")
	BST02 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="00")
	PREFIX_CLIENT = forms.CharField(required=True, label='Client', widget=forms.TextInput(attrs={'class': 'form-control'}))
	PREFIX_NAME = forms.CharField(required=True, label='Client', widget=forms.TextInput(attrs={'class': 'form-control'}))
	CLIENT = forms.CharField(required=True, label='Client', widget=forms.TextInput(attrs={'class': 'form-control'}))
	NAME = forms.CharField(required=True, label='Client', widget=forms.TextInput(attrs={'class': 'form-control'}))
	ST02 = forms.CharField(required=False, label='Transaction Control Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST01 = forms.CharField(required=False, label='Purpose Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST03 = forms.CharField(required=False, label='Date', widget=forms.TextInput(attrs={'class': 'form-control'}))
	BST04 = forms.CharField(required=False, label='Time', widget=forms.TextInput(attrs={'class': 'form-control'}))
	DTM01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="011")
	DTM02 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="0")
	DTM03 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="0")
	DTM04 = forms.CharField(required=False, label='Time Zone', widget=forms.TextInput(attrs={'placeholder': 'Use Mexico Central', 'class': 'form-control'}))
	DTM05 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="21")

	class Meta:
		model = Data_Generator_Master
		fields = ["ST02", "BST01", "BST03", "BST04", "DTM04", "ST01", "CLIENT", "NAME", "PREFIX_NAME", "PREFIX_CLIENT"]

class ASN_Shipment(forms.ModelForm):

	N101 = forms.CharField(required=False, label='Operation', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N102 = forms.CharField(required=False, label='Operation', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N103 = forms.CharField(required=False, label='Identification Method', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N104 = forms.CharField(required=False, label='Identification', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N201 = forms.CharField(required=False, label='Operation', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N202 = forms.CharField(required=False, label='Identification Method', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N203 = forms.CharField(required=False, label='Identification Method', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N204 = forms.CharField(required=False, label='Identification', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N301 = forms.CharField(required=False, label='Operation', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N302 = forms.CharField(required=False, label='Identification', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N303 = forms.CharField(required=False, label='Identification Method', widget=forms.TextInput(attrs={'class': 'form-control'}))
	N304 = forms.CharField(required=False, label='Identification', widget=forms.TextInput(attrs={'class': 'form-control'}))
	HL01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	HL02 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	HL03 = forms.CharField(widget=forms.HiddenInput(), initial="PD")
	MEA01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	MEA02 = forms.CharField(required=False, label='Weight Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA03 = forms.CharField(required=False, label='Weight Value', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA04 = forms.CharField(required=False, label='Weight Unit', widget=forms.TextInput(attrs={'placeholder': 'KG MM L LBS .. ETC', 'class': 'form-control'}))
	TD101 = forms.CharField(required=False, label='Packaging Code', widget=forms.TextInput(attrs={'placeholder': 'No. Guia', 'class':  'form-control'}))
	TD102 = forms.CharField(required=False, label='Landing Quantity', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD501 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="B")
	TD502 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="2")
	TD503 = forms.CharField(required=False, label='ID Code', widget=forms.TextInput(attrs={'placeholder': '','class': 'form-control'}))
	TD504 = forms.CharField(required=False, label='Transportation Method', widget=forms.TextInput(attrs={'placeholder': 'TL','class': 'form-control'}))
	TD507 = forms.CharField(required=False, label='Location Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD508 = forms.CharField(required=False, label='Location ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD301 = forms.CharField(required=False, label='Equipment Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD302 = forms.CharField(required=False, label='Equipment Initial', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD303 = forms.CharField(required=False, label='Equipment Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TD401 = forms.CharField(required=False,  label='Special Handling Code', widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
	TD402 = forms.CharField(required=False, label='Hazardous Qualifier', widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
	TD403 = forms.CharField(required=False,  label='Hazardous Code', widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
	TD404 = forms.CharField(required=False,  label='Description', widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
	TD405 = forms.CharField(required=False,  label='Condition', widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
	REF01 = forms.CharField(required=False, label='Reference Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF02 = forms.CharField(required=False, label='Reference ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Master
		fields = ["MEA02", "MEA03", "MEA04", "TD101", "TD102", "TD503", "TD504", "TD507", "TD508", "TD301", "TD302", "TD303", "TD401", "TD402", "TD403", "TD404", "TD405", "REF01", "REF02", "N101", "N102",
		 "N103", "N104", "N201", "N202", "N203", "N204", "N301", "N302", "N303", "N304" ]


class ASN_Order(forms.ModelForm):
	HL01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	HL02 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	HL03 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	LIN02 = forms.CharField(required=False, label='Product Qualifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
	LIN03 = forms.CharField(required=False, label='Product ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SN102 = forms.CharField(required=False, label='Number of Units Shiped', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SN103 = forms.CharField(required=False, label='Unit', widget=forms.TextInput(attrs={'placeholder': 'Piezas','class': 'form-control'}))
	SN104 = forms.CharField(required=False, label='Quantity Shipped', widget=forms.TextInput(attrs={'class': 'form-control'}))
	PRF01 = forms.CharField(required=False, label='Purchase Order Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF101 = forms.CharField(required=False, label='Reference', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF102 = forms.CharField(required=False, label='Reference', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF201 = forms.CharField(required=False, label='Reference', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF202 = forms.CharField(required=False, label='reference', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Order
		fields = ["LIN02", "LIN03", "SN102", "SN103", "SN104", "PRF01", "REF101", "REF102", "REF201", "REF202"]


class ASN_Item(forms.ModelForm):
	CLD01 = forms.CharField(required=False, label='Number of Loads', widget=forms.TextInput(attrs={'class': 'form-control'}))
	CLD02 = forms.CharField(required=False, label='Units Shipped', widget=forms.TextInput(attrs={'class': 'form-control'}))
	CLD03 = forms.CharField(required=False, label='Packaging Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA01 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	MEA02 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA03 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA04 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA201 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	MEA202 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA203 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA204 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA301 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	MEA302 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA303 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA304 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA401 = forms.CharField(required=False, widget=forms.HiddenInput(), initial="PD")
	MEA402 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA403 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	MEA404 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD101 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD102 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD201= forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD202 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD301 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD302 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD401 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD402 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_ITEM101 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_ITEM102 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Hierarchial
		fields = ["CLD01", "CLD02", "CLD03"]


class ASN_Item2(forms.ModelForm):
	REF_CLD1 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	REF_CLD2 = forms.CharField(required=False, label='Measure', widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Data_Generator_Loads
		fields = ["REF_CLD1", "REF_CLD2"]