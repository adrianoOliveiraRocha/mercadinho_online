from django import template

register = template.Library()

@register.simple_tag
def show_status(status):
	if status == 'A':
		return 'Ativo'
	elif status == 'I':
		return 'Inativo'

@register.simple_tag
def show_status_pg(status):
	if status == '1':
		return 'Completo'
	elif status == '2':
		return 'Aprovado'
	elif status == '3':
		return 'Em Análise'
	elif status == '4':
		return 'Devolvido'
	elif status == '5':
		return 'Cancelado'

@register.simple_tag
def get_value(quantity, value):
	return float(quantity) * float(value)
	
