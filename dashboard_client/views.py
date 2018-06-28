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
		form = ClientForm(request.POST, instance=client)
		if form.is_valid():
			if form.has_changed():
				client.name = form.cleaned_data['name']
				client.email = form.cleaned_data['email']
				client.telefone = form.cleaned_data['telefone']
				client.cpf = form.cleaned_data['cpf']
				client.logradouro = form.cleaned_data['logradouro']
				client.numero = form.cleaned_data['numero']
				client.cep = form.cleaned_data['cep']
				client.complemento = form.cleaned_data['complemento']
				client.bairro = form.cleaned_data['bairro']
				client.cidade = form.cleaned_data['cidade']
				client.estado = form.cleaned_data['estado']
				messages.success(request,
					'Os dados foram alterados com sucesso!')
				client.save()
			else:
				messages.warning(request,
					'Os dados não foram alterados')
		else:
			for error in form.errors:
				print(error)	
		return HttpResponseRedirect(reverse('dashboard_client:index'))
		



	