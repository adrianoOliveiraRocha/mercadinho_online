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
	path('delete_orderitem/<int:orderitem>',
		views.delete_orderitem, name='delete_orderitem'),
	path('cancel_order/<int:order_id>',
		views.cancel_order, name='cancel_order'),
	path('send_order/<int:order_id>', views.send_order,
		name='send_order'),
	path('my_orders/', views.my_orders,
		name='my_orders'),
	path('order_detail/<int:order_id>', views.order_detail,
		name='order_detail'),
		
]