from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import UserAdminCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserAdminForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import resolve_url


class RegisterView(CreateView):
	model = User
	form_class = UserAdminCreationForm
	template_name = "accounts/register.html"
	
	success_url = reverse_lazy('login') 


@login_required
def registration_data(request):
	""" edit client """
	user = User.objects.get(id=request.user.id)
	if request.method == 'GET':
		form = ClientForm(instance=user)
		context = {'form': form}

		return render(request, 'checkout/registration_data.html', context)
	else:
		form = ClientForm(request.POST, instance=user)
		context = {'form': form}
		if form.is_valid():
			user.save()
			messages.add_message(request, messages.INFO,
				"Alterações salvas com sucesso!")
			
		return render(request, 'checkout/registration_data.html', context)


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Sua senha foi atualizada com sucesso!')
			return HttpResponseRedirect(reverse('accounts:my_data'))
		else:
			print(form.errors)
			messages.success(request, 'Por favor, corrija o erro abaixo!')
	else:
		form = PasswordChangeForm(request.user)
		
	return render(request, 'accounts/change_password.html',
		{'form': form})


@login_required
def registration_data(request):
	""" edit client """
	user = User.objects.get(id=request.user.id)
	if request.method == 'GET':
		form = ClientForm(instance=user)
		context = {'form': form}

		return render(request, 'checkout/registration_data.html', context)
	else:
		form = ClientForm(request.POST, instance=user)
		context = {'form': form}
		if form.is_valid():
			user.save()
			messages.add_message(request, messages.INFO,
				"Alterações salvas com sucesso!")
			
		return render(request, 'checkout/registration_data.html', context)


@login_required
def my_data(request):
	user = User.objects.get(id=request.user.id)
	context = {}
	if request.method == 'GET':
		form = UserAdminForm(instance=user)
		context.update({'form': form})
		
	if request.method == 'POST':
		form = UserAdminForm(request.POST, instance=user)
		context.update({'form': form})
		if form.is_valid():
			form.save()
			messages.success(request, 'Dados alterados com sucesso!')

	return render(request, 'accounts/my_data.html', context)


@login_required
def new_member(request):
	context = {'new_member': True}
	if request.method == 'GET':
		form = UserAdminCreationForm()
		context['form'] = form
		return render(request, 'accounts/register.html', context)
		
	else:
		form = UserAdminCreationForm(request.POST)
		context['form'] = form
		if form.is_valid():
			user = User()
			user.username = form.cleaned_data['username']
			user.name = form.cleaned_data['name']
			user.email = form.cleaned_data['email']
			user.telefone = form.cleaned_data['telefone']
			user.cpf = form.cleaned_data['cpf']
			user.logradouro = form.cleaned_data['logradouro']
			user.numero = form.cleaned_data['numero']
			user.cep = form.cleaned_data['cep']
			user.complemento = form.cleaned_data['complemento']
			user.bairro = form.cleaned_data['bairro']
			user.estado = form.cleaned_data['estado']
			user.is_staff = True
			user.set_password(form.cleaned_data['password1'])
			user.save()
			messages.success(request, 'Novo membro da equipe criado com sucesso!')
			url = resolve_url('/area_administrativa/index')
			return HttpResponseRedirect(url)
		else:
			return render(request, 'accounts/register.html', context)
	
