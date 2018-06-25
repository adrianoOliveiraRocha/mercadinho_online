from django.urls import path
from . import views

app_name = 'dashboard_admin'

urlpatterns = [
	path('', views.index, name='index'),
	path('new_category', views.new_category, name='new_category'),
	path('show_all_categories', views.show_all_categories, 
		name='show_all_categories')
]