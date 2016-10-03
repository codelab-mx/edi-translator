from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.edi_index, name='view_edis'),
    url(r'^ver/(?P<edi_viewer>[0-9]+)/$', views.edi_viewer, name='edi_viewer'),
    url(r'^traducir/$', views.edi_translator, name='edi_translator'),
    url(r'^traducir/(?P<edi>[0-9]+)/$', views.edi_translate, name='edi_exe'),
    url(r'^delete_edi/(?P<edi>\d+)/$', views.delete_edi, name='edi_delete'),
]