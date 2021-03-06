from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from catalog.models import Product
from core import utils
from accounts.models import User
from django.contrib import messages
from django.shortcuts import resolve_url


@login_required
def insert_cart(request, product_id):
	context = {}
	nItems = 0
	if 'order_id' in request.session:
		order = Order.objects.get(id=request.session['order_id'])
		orderItem = OrderItem()
		product = Product.objects.get(id=product_id)
		orderItem.order = order
		orderItem.product = product
		orderItem.value = product.value
		orderItem.save()
		# context['order'] = order
		# context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		request.session['howItems'] = \
		int(request.session['howItems']) + 1
		
	else:
		order = Order()
		order.user = User.objects.get(id=request.user.id)
		order.save()

		orderItem = OrderItem()
		product = Product.objects.get(id=product_id)
		orderItem.order = order
		orderItem.product = product
		orderItem.value = product.value
		orderItem.save()
		# context['order'] = order
		# context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		request.session['order_id'] = order.id 
		request.session['howItems'] = 1
		
	
	return HttpResponseRedirect(resolve_url("/"))

