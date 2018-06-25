from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from catalog.models import Category, Product
from catalog.forms import CategoryForm, ProductForm
from django.contrib import messages
from core.utils import Utils


@login_required
def index(request):
	user = User.objects.get(id=request.user.id)
	if user.is_staff:
		return render(request, 'dashboard_admin/index.html')
	else:
		return HttpResponse('Acesso não permitido!')


@login_required
def new_category(request):
	context = {}
	
	if request.method == 'GET':
		form = CategoryForm()
		context['form'] = form
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
		
	return render(request, 'dashboard_admin/new_category.html',
		context)


@login_required
def show_all_categories(request):
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'dashboard_admin/show_all_categories.html',
		context)


@login_required
def edit_category(request, id_category):

	context = {}
	category = Category.objects.get(id=id_category)
	
	if request.method == 'GET':
		form = CategoryForm(instance=category)
		context['form'] = form	
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
def new_product(request):
	context = {}
	
	if request.method == 'GET':
		form = ProductForm()
		context['form'] = form
	else:
		form = ProductForm(request.POST)
		if form.is_valid():
			value = Utils.convertStringForNumber(
				request.POST.get('value'))
			product = form.save()
			product.value = value
			product.save()
			messages.success(request,
				"Novo Produto salvo com sucesso!")
		else:
			messages.warning(request,
				"Por favor, preencha os campos corretamente!")
		context['form'] = form
		
	return render(request, 'dashboard_admin/new_product.html',
		context)