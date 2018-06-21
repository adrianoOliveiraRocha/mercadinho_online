from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
# from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from catalog.models import Category
from django.core.paginator import Paginator


User = get_user_model()

def index(request):
	all_categories = Category.objects.all()
	context = {
		'all_categories': all_categories,
	}
	return render(request, 'core/index.html',
		context)


class QuemSomosView(TemplateView):
	template_name = "core/quem_somos.html"


class ContatctView(TemplateView):
	template_name = "core/contato.html"



