from django.urls import path
from . import views

app_name = 'dashboard_admin'

urlpatterns = [
	path('', views.index, name='index'),
	path('new_category', views.new_category, name='new_category'),
	path('new_product', views.new_product, name='new_product'),
	path('todas_as_categorias', views.show_all_categories, 
		name='show_all_categories'),
	path('edit_category/<int:id_category>', views.edit_category,
		name='edit_category')
]