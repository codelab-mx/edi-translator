from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tradings_index, name='view_tradings'),
    url(r'^new_company/$', views.new_company, name='new_company'),
    url(r'^edit_company/(?P<company_id>[0-9]+)/$', views.edit_company, name='edit_company'),
    url(r'^view_company/(?P<company_id>[0-9]+)/$', views.view_company, name='view_company'),
    url(r'^delete_company/(?P<company_id>[0-9]+)/$', views.delete_company, name='delete_company'),
    url(r'^new_partner/$', views.new_partner, name='new_partner'),
    url(r'^edit_partner/(?P<partner_id>[0-9]+)/$', views.edit_partner, name='edit_partner'),
    url(r'^view_partner/(?P<partner_id>[0-9]+)/$', views.view_partner, name='view_partner'),
    url(r'^delete_partner/(?P<partner_id>[0-9]+)/$', views.delete_partner, name='delete_partner'),
]