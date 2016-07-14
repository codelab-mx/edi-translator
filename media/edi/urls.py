from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views
#from gaia.views import sae_index, sae_login

urlpatterns = [
	url(r'^$', views.login, {'template_name':'access/login.html'}, name='home'),
	url(r'^logout/$', views.logout_then_login, name='logout'),
	url(r'^admin/', admin.site.urls),
]

#	url(r'^$', sae_login),
#   url(r'^admin/', admin.site.urls),
