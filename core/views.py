from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from catalog.models import Category, Product
from django.core.paginator import Paginator
from django.contrib import messages
from checkout.models import Order

User = get_user_model()

def index(request):
	# request.session.clear()
	print('core/index')
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

	if request.user.is_authenticated:
		order = Order.objects.filter(sended=False).\
		filter(user__id=request.user.id).first()
		if order:
			request.session['order_id'] = order.id
			request.session['howItems'] = Order.orderManager.howMayOrderItem(order.id)
		else:
			print("There ins't order")

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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context




class ContatctView(TemplateView):
	template_name = "core/contato.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context



