from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.usuarios, name='usuarios'),
    url(r'^nuevo/(?P<grupo>[-\w.]+)/$', views.usuario_nuevo, name='nuevo_usuario'),
    url(r'^ver/(?P<user_name>[-\w.]+)/$', views.ver_usuario, name='ver_usuario'),
    url(r'^eliminar/(?P<user_name>[-\w.]+)/$', views.eliminar_usuario, name='eliminar_usuario'),
]