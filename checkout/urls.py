from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
	path('insert_cart/<int:product_id>', views.insert_cart,
		name='insert_cart'),
	
]