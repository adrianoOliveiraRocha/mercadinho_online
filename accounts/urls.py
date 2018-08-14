from django.urls import include, path
from django.contrib.auth.views import login, logout
from . import views 

app_name = 'accounts'

urlpatterns = [
	path('registro', views.RegisterView.as_view(), name='register'),
	path('registration_data', views.registration_data,
		name='registration_data'),
	path('change_password', views.change_password, name='change_password'),
	path('my_data/', views.my_data, name='my_data'),
	path('trocar_senha', views.change_password, name='change_password'),
	path('novo_membro', views.new_member, name='new_member'),
	
]