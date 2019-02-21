from django.shortcuts import render, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from catalog.models import Category, Product
from catalog.forms import CategoryForm, ProductForm
from django.contrib import messages
from core.utils import Utils
from django.urls import reverse
from checkout.models import Order, OrderItem

def noForwardedsInfo(request):
	""" This function update the information about orders no forwarded and 
	return the object orderSended. Some functions need no use this object """
	ordersSendeds = Order.objects.filter(sended=True)
	request.session['no_forwarded'] = Order.getNoForwardeds(ordersSendeds)
	return ordersSendeds

@login_required
def index(request):
	ordersSendeds = noForwardedsInfo(request)
	user = User.objects.get(id=request.user.id)
	context = {
		'orders': ordersSendeds,
	}

	if user.is_staff:
		return render(request, 'dashboard_admin/index.html',
			context)
	else:
		return HttpResponse('Acesso não permitido!')


@login_required
def new_category(request):
	noForwardedsInfo(request)
	context = {}
	
	if request.method == 'GET':
		form = CategoryForm()
		context['form'] = form
		return render(request, 'dashboard_admin/new_category.html',
			context)
	else:
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save()
			category.save()
			messages.success(request,
				"Nova categoria salva com sucesso!")
		else:
			messages.warning(request,
				"Por favor, preencha os campos corretamente!")

		context['form'] = form
		return HttpResponseRedirect(
			reverse('dashboard_admin:show_all_categories'))


@login_required
def show_all_categories(request):
	noForwardedsInfo(request)
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'dashboard_admin/show_all_categories.html',
		context)

@login_required
def show_all_products(request):
	noForwardedsInfo(request)
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'dashboard_admin/show_all_products.html',
		context)


@login_required
def edit_category(request, id_category):
	noForwardedsInfo(request)
	context = {}
	category = Category.objects.get(id=id_category)
	
	if request.method == 'GET':
		form = CategoryForm(instance=category)
		context['form'] = form	
		context['id_category'] = category.id
	else:
		form = CategoryForm(request.POST)
		context['form'] = form
		if form.is_valid():
			category.name = form.cleaned_data['name']
			category.save()
			messages.success(request,
				'Categoria editada com secesso!')
		else:
			messages.warning(request,
				'Por favor, preencha os dados corretamente!')


	return render(request, 'dashboard_admin/edit_category.html',
		context)


@login_required
def edit_product(request, id_product):
	noForwardedsInfo(request)
	context = {}
	product = Product.objects.get(id=id_product)
		
	if request.method == 'GET':
		form = ProductForm(instance=product)
		context['form'] = form	
		context['value'] = product.value
		context['id_product'] = product.id
		return render(request, 'dashboard_admin/edit_product.html',
			context)
	else:
		form = ProductForm(request.POST, request.FILES)
		context['form'] = form
		if form.is_valid():
			value = Utils.convertStringForNumber(
				request.POST.get('value'))
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']

			if form.cleaned_data['image']:
				product.image = form.cleaned_data['image']

			product.brand = form.cleaned_data['brand']
			product.category = form.cleaned_data['category']
			product.value = value
			product.save()
			messages.success(request,
				'Produto editado com secesso!')
		else:
			messages.warning(request,
				'Por favor, preencha os dados corretamente!')

		return HttpResponseRedirect(
			reverse('dashboard_admin:show_all_products'))

	


@login_required
def new_product(request):
	noForwardedsInfo(request)
	context = {}
	
	if request.method == 'GET':
		form = ProductForm()
		context['form'] = form
		return render(request, 'dashboard_admin/new_product.html',
			context)
	else:
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			value = Utils.convertStringForNumber(
				request.POST.get('value'))
			product = Product()
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.image = form.cleaned_data['image']
			product.value = value
			product.brand = form.cleaned_data['brand']
			product.category = form.cleaned_data['category']
			product.save()
			messages.success(request,
				"Novo Produto salvo com sucesso!")
		else:
			messages.warning(request,
				"Por favor, preencha os campos corretamente!")
		context['form'] = form

		return HttpResponseRedirect(reverse('dashboard_admin:show_all_products'))


@login_required
def delete_category(request, id_category):
	category = Category.objects.get(id=id_category)
	category.delete()
	messages.success(request, 
		"Categoria deletada com sucesso!")
	return HttpResponseRedirect(
		reverse('dashboard_admin:show_all_categories'))


@login_required
def delete_product(request, id_product):
	product = Product.objects.get(id=id_product)
	product.delete()
	messages.success(request, 
		"Produto deletado com sucesso!")
	return HttpResponseRedirect(
		reverse('dashboard_admin:show_all_products'))


@login_required
def order_datail(request, order_id):
	noForwardedsInfo(request)
	order = Order.objects.get(id=order_id)
	items = OrderItem.objects.filter(order=order_id)
	context = {
		'order': order,
		'items': items
		}
	return render(request, 'dashboard_admin/order_datail.html',
		context)
	

@login_required
def forward(request, order_id):
	order = Order.objects.get(id=order_id)
	order.forwarded = True
	order.save()
	
	request.session['no_forwarded'] = \
		int(request.session['no_forwarded']) - 1
	if int(request.session['no_forwarded']) <= 0:
		del request.session['no_forwarded']

	messages.success(request, 
		"Pedido Encaminhado!")
	url = '/area_administrativa/detalhes_do_pedido/{}'.format(order_id)
	return HttpResponseRedirect(resolve_url(url))


@login_required
def forwarded(request):
	orders = Order.objects.filter(forwarded=True)
	context = {
		'orders': orders
	}
	return render(request, 'dashboard_admin/forwarded.html',
		context)


@login_required
def no_forwarded(request):
	orders = Order.objects.filter(forwarded=False)
	context = {
		'orders': orders
	}

	return render(request, 'dashboard_admin/no_forwarded.html',
		context)