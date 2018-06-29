from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from catalog.models import Product
from core import utils
from accounts.models import User
from django.contrib import messages


@login_required
def insert_cart(request, product_id):
	context = {}
	if 'order_id' in request.session:
		order = Order.objects.get(id=request.session['order_id'])
		
		orderItem = OrderItem()
		product = Product.objects.get(id=product_id)
		orderItem.order = order
		orderItem.product = product
		orderItem.value = product.value
		orderItem.save()
		context['order'] = order
		context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		messages.success(request, 'Produto inserido no carrinho')
		print(order)
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
		context['order'] = order
		context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		request.session['order_id'] = order.id 
		print(order)
	return render(request, "dashboard_client/cart.html",
		context)


@login_required
def cart(request):
	context = {}
	if 'order_id' in request.session:
		order = Order.objects.get(id=request.session['order_id'])
		context['order'] = order
		context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		
	else:
		messages.warning(request, 'Seu carrinho está vazio')
	return render(request, "dashboard_client/cart.html",
		context)