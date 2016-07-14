from django.core.exceptions import ValidationError

def file_size(value):
	limit = 10 * 1024
	if value.size > limit:
		raise ValidationError('El Archivo EDI no debe de pesar mas de 10 MB')