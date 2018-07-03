from django.urls import path
from . import views

app_name = 'dashboard_client'

urlpatterns = [
	path('', views.index, name='index'),
	path('meus_dados', views.my_data, name='my_data'),
	path('change_password', views.change_password,
		name='change_password'),
	path('update_value/<int:orderitem>/<int:quantity>',
		views.update_value, name='update_value'),
]