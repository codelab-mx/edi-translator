from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^ver/$', views.render_list, name='render_list'),
    url(r'^ver/(?P<master_id>[0-9]+)/$', views.index_render, name='render_edi'),
    url(r'^856/$', views.ASN_New, name='856'),
    url(r'^856/(?P<master_id>[0-9]+)/shipment/(?P<cont>[0-9]+)/$', views.ASN_New_Shipment, name='856_shipment'),
    url(r'^856/(?P<master_id>[0-9]+)/order/(?P<cont>[0-9]+)/$', views.ASN_New_Order, name='856_order'),
    url(r'^856/(?P<master_id>[0-9]+)/item/(?P<cont>[0-9]+)/$', views.ASN_New_Item, name='856_item'),
    url(r'^856/(?P<master_id>[0-9]+)/load/(?P<cont>[0-9]+)/$', views.New_Load, name='856_load'),
     url(r'^delete_edi/(?P<master_id>\d+)/$', views.delete_edi, name='delete_edi'),
    #url(r'^traducir/$', views.edi_translator, name='traducir'),
    #url(r'^traducir/(?P<edi>[0-9]+)/$', views.edi_translate, name='ejecutar'),
]