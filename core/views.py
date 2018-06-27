from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from catalog.models import Category, Product
from django.core.paginator import Paginator


User = get_user_model()

def index(request):
	categories = Category.objects.all()
	product_list = Product.objects.all()
	paginator = Paginator(product_list, 6)
	page = request.GET.get('page')
	products = paginator.get_page(page)

	label_category = 'TODAS AS CATEGORIAS'

	context = {
		'label_category': label_category,
		'categories': categories,
		'products': products,
		'paginator': paginator,
	}

	return render(request, 'core/index.html',
		context)


def category(request, category_id):
	categories = Category.objects.all()
	product_list = Product.objects.filter(category__id=category_id)
	paginator = Paginator(product_list, 6)
	page = request.GET.get('page')
	products = paginator.get_page(page)

	label_category = str.upper(Category.objects.get(id=category_id).name)

	context = {
		'label_category': label_category,
		'categories': categories,
		'products': products,
		'paginator': paginator,
	}
	
	return render(request, 'core/index.html',
		context)


class QuemSomosView(TemplateView):
	template_name = "core/quem_somos.html"


class ContatctView(TemplateView):
	template_name = "core/contato.html"



