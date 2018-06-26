from django.urls import path
from . import views

app_name = 'dashboard_client'

urlpatterns = [
	path('', views.index, name='index'),
	path('meus_dados', views.my_data, name='my_data')
]