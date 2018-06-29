from django.db import models
from catalog.models import Product
from datetime import date
from accounts.models import User

STATUS_ORDER = (
			('A', 'active'), 
			('I', 'INACTIVE'),
		)

STATUS_PAGSEGURO = (
		('1', 'Completo'), ('2', 'Aprovado'), 
		('3', 'Em Análise'), ('4', 'Devolvido'),
		('5', 'Cancelado')
	)

class Order(models.Model):
	date = models.DateField(default=date.today, editable=False)
	value = models.DecimalField('Valor R$', max_digits=10,
		decimal_places=2, default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE,
		null=True, blank=True)
	delivery_address_is_the_same = models.BooleanField(
		verbose_name='Entregar no endereço cadastrado',
		default=True,
		blank=True)
	logradouro = models.CharField('Rua/Avenida', max_length=100,
		null=True, blank=True, default='')
	numero = models.CharField('Número', max_length=100,
		null=True, blank=True, default='')
	cep = models.CharField('CEP', max_length=10, null=True, 
		blank=True, default='')
	complemento = models.CharField('Complamento', max_length=100, 
		null=True, blank=True, default='')
	bairro = models.CharField('Bairro', max_length=100, null=True, 
		blank=True, default='')
	cidade = models.CharField('Cidade', max_length=100, null=True,
		blank=True, default='')
	estado = models.CharField('Estado', max_length=100, null=True,
		blank=True, default='')
	transaction_id = models.CharField('ID da transação', max_length=100,
		null=True, blank=True)
	status_order = models.CharField('Status do Pedido', max_length=10,
		choices=STATUS_ORDER, default='A') 
	status_pg = models.CharField('Status PagSeguro', max_length=10,
		choices=STATUS_PAGSEGURO, null=True, blank=True)

	def __str__(self):
		return 'Pedido realizado em {}'.format(self.user, self.date)

	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'
		ordering = ['date']


class OrderItem(models.Model):
	quantity = models.PositiveSmallIntegerField(verbose_name='Quantidade',
		default=1, editable=False)
	value = models.DecimalField('Valor R$', max_digits=10,
		decimal_places=2, default=0)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Ítem de Pedido'
		verbose_name_plural = 'Ítens de Pedido'
		ordering = ['order']