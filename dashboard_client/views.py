from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import User
from django.contrib import messages
from core.utils import Utils
from django.urls import reverse
from accounts.forms import ClientForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from checkout.models import Order, OrderItem


@login_required
def index(request):
	# search for order that had status active
	order = Order.objects.filter(user__id=request.user.id).\
	filter(status_order='A').first()
	
	context = {}

	if order:
		context['order'] = order
		context['orderItems'] = OrderItem.objects.filter(order__id=order.id)
		context['total'] = OrderItem.get_total(order.id)
	else:
		messages.warning(request, 'Você não tem nenhum pedido ativo')

	return render(request, 'dashboard_client/index.html',
		context)


@login_required
def send_order(request, order_id):
	context = {'order_id': order_id}
	return render(request, 'dashboard_client/send_order.html', 
		context)


@login_required
def send_to_admin(request, order_id):
	order = Order.objects.get(id=order_id)
	items = OrderItem.objects.filter(order=order_id)
	order.value = OrderItem.get_total(items)
	order.sended = True
	order.save()
	return render(request, 'dashboard_client/sended.html')


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
		

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Sua senha foi atualizada com sucesso!')
			return HttpResponseRedirect(reverse('dashboard_client:my_data'))
		else:
			messages.success(request, 'Por favor, corrija o erro abaixo!')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'dashboard_client/change_password.html',
		{'form': form})


@login_required
def update_value(request, orderitem, quantity):
	orderItem = OrderItem.objects.get(id=orderitem)
	productPrice = orderItem.product.value
	orderItem.quantity = quantity
	orderItem.value = quantity * productPrice
	orderItem.save()
	return HttpResponseRedirect(reverse('dashboard_client:index'))


@login_required
def delete_orderitem(request, orderitem):
	orderItem = OrderItem.objects.get(id=orderitem)
	orderItem.delete()
	request.session['howItems'] = \
	int(request.session['howItems']) - 1
	order = Order.objects.get(id=orderItem.order.id)
	if not Order.orderManager.hasOrderItem(order.id):
		order.delete()
		del request.session['order_id']
		del request.session['howItems']
		
	return HttpResponseRedirect(reverse('dashboard_client:index'))
	

@login_required
def cancel_order(request, order_id):
	order = Order.objects.get(id=order_id)
	order.delete()
	del request.session['order_id']
	del request.session['howItems']
	return HttpResponseRedirect(reverse('dashboard_client:index'))