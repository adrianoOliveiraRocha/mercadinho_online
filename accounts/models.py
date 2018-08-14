# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
	UF_CHOICES = (
    ('AC','Acre'), ('AL','Alagoas'), ('AP','Amapá'),
    ('AM','Amazonas'), ('BA','Bahia'), ('CE','Ceará'),
    ('DF','Distrito Federal'), ('ES','Espírito Santo'),
    ('GO','Goiás'), ('MA','Maranhão'), ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'), ('MG','Minas Gerais'),
    ('PA','Pará'), ('PB','Paraíba'), ('PR','Paraná'),
    ('PE','Pernambuco'), ('PI','Piauí'),
    ('RJ','Rio de Janeiro'), ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'), ('RO','Rondônia'),
    ('RR','Roraima'), ('SC','Santa Catarina'),
    ('SP','São Paulo'), ('SE','Sergipe'),
	('TO','Tacantins'), )
	username = models.CharField(
		'Login', max_length=30, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um nome de usuário válido. '
				'Este valor deve conter apenas letras, números '
				'e os caracteres: @/./+/-/_ .'
				, 'invalid'
			)
		], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
	)
	name = models.CharField('Nome', max_length=100, blank=True)
	email = models.EmailField('E-mail', unique=True)
	telefone = models.CharField('Telefone', max_length=20, null=True,
		blank=True)
	cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
	logradouro = models.CharField('Rua/Avenida', max_length=100,
		null=True, blank=True)
	numero = models.CharField('Número', max_length=100,
		null=True, blank=True)
	cep = models.CharField('CEP', max_length=10, null=True, blank=True)
	complemento = models.TextField('Complamento', max_length=100, 
		null=True, blank=True)
	bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)
	cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
	estado = models.CharField('Estado', max_length=100, null=True, blank=True,
		choices=UF_CHOICES)
	
	is_staff = models.BooleanField('Equipe', default=False)
	is_active = models.BooleanField('Ativo', default=True)
	date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

	def __str__(self):
		return self.name or self.username

	def get_full_name(self):
		return str(self)

	def get_short_name(self):
		return str(self).split(" ")[0]

	@staticmethod
	def get_all_clients():
		""" get all users that is not staff """
		all_clients = []
		users = User.objects.all()
		for user in users:
			if not user.is_staff:
				all_clients.append(user)
		return all_clients
	
	@staticmethod
	def get_all_members():
		""" get all users that is staff """
		all_members = []
		users = User.objects.all()
		for user in users:
			if user.is_staff:
				all_members.append(user)
		return all_members

	
