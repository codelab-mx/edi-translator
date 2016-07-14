from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.usuarios, name='usuarios'),
    url(r'^nuevo/(?P<grupo>[\w-]+)$', views.usuario_nuevo, name='nuevo'),
    url(r'^ver/(?P<user_name>[\w-]+)/$', views.ver_usuario, name='ver'),
]