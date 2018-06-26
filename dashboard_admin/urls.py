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
		name='edit_category'),
	path('edit_product/<int:id_product>', views.edit_product,
		name='edit_product'),
	path('delete_categoria/<int:id_category>', views.delete_category,
		name='delete_category'),
	path('delete_produto/<int:id_product>', views.delete_product,
		name='delete_product'),
	path('todos_os_produtos', views.show_all_products, 
		name='show_all_products'),
]