from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from catalog.models import Category, Product
from catalog.forms import CategoryForm
from django.contrib import messages


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
			messages.warning(request,
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