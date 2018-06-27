from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from django.contrib import messages
from core.utils import Utils
from django.urls import reverse
from accounts.forms import ClientForm


@login_required
def index(request):
	return render(request, 'dashboard_client/index.html')


@login_required
def my_data(request):

	client = User.objects.get(id=request.user.id)
	if request.method == 'GET':
		form = ClientForm(instance=client)
		context = {'form': form}
		return render(request, 'dashboard_client/my_data.html',
			context)
	else:
		form = ClientForm(request.POST)
		context = {'form': form}
		if form.is_valid():
			if form.has_changed():
				client.username = form.clened_date['username']
				client.name = form.clened_date['name']
				client.email = form.clened_date['email']
				client.telefone = form.clened_date['telefone']
				client.cpf = form.clened_date['cpf']
				client.logradouro = form.clened_date['logradouro']
				client.numero = form.clened_date['numero']
				client.cep = form.clened_date['cep']
				client.complemento = form.clened_date['complemento']
				client.bairro = form.clened_date['bairro']
				client.cidade = form.clened_date['cidade']
				client.estado = form.clened_date['estado']
				client.save()
				messages.success(request,
					"Alterações realizadas com sucesso!")
				
			else:
				messages.success(request,
					"Nenhuma alteração foi realizada")
			return HttpResponse(
					render('dashboard_client:index')
				)
		else:
			messages.warning(request,
				"O formulário não foi preenchido corretamente")
			return render(request, 'dashboard_client/my_data.html',
				context)



	