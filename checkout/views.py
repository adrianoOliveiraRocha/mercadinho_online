from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from catalog.models import Product
from core import utils
from accounts.models import User


@login_required
def insert_cart(request, product_id):
	if 'order_id' in request.session:
		order = Order.objects.get(id=request.session['order_id'])

		orderItem = OrderItem()
		product = Product.objects.get(id=product_id)
		orderItem.order = order
		orderItem.product = product
		orderItem.value = product.value
		orderItem.save()
		return HttpResponse('More one product were add')

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

		request.session['order_id'] = order.id 
		return HttpResponse('I create the session variable that keep\
		 the order id')
