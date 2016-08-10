from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^edi/', include('data_mining.urls')),
	url(r'^tradings/', include('address.urls')),
	url(r'^crear/', include('data_generator.urls')),
	url(r'^usuarios/', include('usuarios.urls')),
	url(r'^login/', views.login_crm, name='login'),
	url(r'^logout/', views.logout_crm),
	url(r'^setup/', views.setup, name='setup'),
	url(r'^admin/', admin.site.urls),
]
