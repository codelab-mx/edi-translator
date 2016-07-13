import os
import sys
sys.path.append('/home/zardain/Documents/Proyectos/edi-translator/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from data_mining.models import Modelo_GS
from django.core.wsgi import get_wsgi_application




m = Modelo_GS()
m.GS_3 = 'soyuneditraducido'
m.save()
