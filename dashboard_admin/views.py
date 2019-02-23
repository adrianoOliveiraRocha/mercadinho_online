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
from reportlab.platypus import (SimpleDocTemplate, Paragraph, 
	Spacer, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from django.core.files.storage import FileSystemStorage
from core.utils import Utils

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

@login_required
def make_pdf(request, order_id):
	# order
	order = Order.objects.get(id=order_id);
	# client
	client = User.objects.get(id=order.user.id)
	# order items
	order_items = OrderItem.objects.filter(order=order_id)

	doc = SimpleDocTemplate("/tmp/report.pdf")
	Catalog = []
	styles = getSampleStyleSheet()
	style = styles['Normal']
	# informations about the order
	header = Paragraph("Pedido {}".format(order.id), styles["Heading1"])
	Catalog.append(header)
	Catalog.append(Spacer(1, 1))

	# Cliente
	txt_intro_orders = "Cliente: {}<br /> Telefone: {}<br /> "\
		"Logradouro: {}<br /> Número: {}<br />".format(client.name, client.telefone, 
		client.logradouro, client.numero)
	p = Paragraph(txt_intro_orders, styles['Heading3'])
	Catalog.append(p)
	Catalog.append(Spacer(1, 1))

	# order items
	text_order_items = """ Ítens do Pedido<br /> <br />"""
	for order_item in order_items:
		text_order_items += """
		Produto:   {}<br />
		Valor:     R$ {}<br />
		Quantidade {}<br />
		Subtotal   R$ {}<br />
		<br />
		""".format(order_item.product.name, order_item.value, 
		order_item.quantity, Utils.orderItemValue(order_item.value, order_item.quantity))
	
	p = Paragraph(text_order_items, styles['Heading3'])
	Catalog.append(p)
	Catalog.append(Spacer(1, 1))

	# values
	text_values = """
	Total:   R$ {}<br />
	Dinheiro R$ {}<br />
	Troco    R$ {}<br />
	""".format(order.value, order.money, (order.money - order.value))
	p = Paragraph(text_values, styles['Heading3'])
	Catalog.append(p)
	Catalog.append(Spacer(1, 1))

	doc.build(Catalog)
	fs = FileSystemStorage("/tmp")
	with fs.open("report.pdf") as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment'; filename="relatorio.pdf"
	return response