from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.edi_index, name='edi'),
    url(r'^generar/$', views.edi_generator, name='generar'),
    url(r'^traducir/$', views.edi_translator, name='traducir'),
    url(r'^traducir/(?P<edi>[0-9]+)/$', views.edi_translate, name='ejecutar'),
]