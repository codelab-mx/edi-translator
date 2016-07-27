from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.edi_index, name='edi'),
    url(r'^856/$', views.ASN_New, name='856'),
    url(r'^856/(?P<master_id>[0-9]+)/shipment/(?P<cont>[0-9]+)/$', views.ASN_New_Shipment, name='856'),
    url(r'^856/(?P<master_id>[0-9]+)/order/(?P<cont>[0-9]+)/$', views.ASN_New_Order, name='856'),
    url(r'^856/(?P<master_id>[0-9]+)/item/(?P<cont>[0-9]+)/$', views.ASN_New_Item, name='856'),
    #url(r'^traducir/$', views.edi_translator, name='traducir'),
    #url(r'^traducir/(?P<edi>[0-9]+)/$', views.edi_translate, name='ejecutar'),
]