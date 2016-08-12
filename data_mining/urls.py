from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.edi_index, name='edi'),
    url(r'^ver/(?P<edi_viewer>[0-9]+)/$', views.edi_viewer, name='ver'),
    url(r'^traducir/$', views.edi_translator, name='traducir'),
    url(r'^traducir/(?P<edi>[0-9]+)/$', views.edi_translate, name='ejecutar'),
    url(r'^delete_edi/(?P<edi>\d+)/$', views.delete_edi, name='delete_edi'),
]