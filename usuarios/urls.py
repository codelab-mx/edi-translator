from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.usuarios, name='usuarios'),
    url(r'^nuevo/(?P<grupo>[\w-]+)$', views.usuario_nuevo, name='nuevo'),
    url(r'^ver/(?P<id>[0-9]+)/$', views.ver_usuario, name='ver'),
]