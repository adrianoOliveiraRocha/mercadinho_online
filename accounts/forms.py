# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from .models import User

# this form create user
class UserAdminCreationForm(UserCreationForm):

	class Meta:
		model = User
		# informations showed when create use
		fields = ['username', 'email', 'name', 'cpf', 'telefone', 'logradouro',
		'numero', 'cep', 'complemento', 'bairro', 'estado']

# this form edit user
class UserAdminForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'name', 'cpf', 'telefone', 'logradouro',
		'numero', 'cep', 'complemento', 'bairro', 'estado']


class ClientForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'name', 'cpf', 'telefone', 'logradouro',
		'numero', 'cep', 'complemento', 'bairro', 'estado']

