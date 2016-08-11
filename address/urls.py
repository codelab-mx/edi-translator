from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tradings_index, name='view_tradings'),
    url(r'^new_company/$', views.new_company, name='new_company'),
    url(r'^new_partner/$', views.new_partner, name='new_partner'),
]