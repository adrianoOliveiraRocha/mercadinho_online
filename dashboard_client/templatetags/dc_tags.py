from django import template

register = template.Library()

@register.simple_tag
def forwarded(value):
	if value:
		return "Sim"
	else:
		return "Não"


@register.simple_tag
def get_value(quantity, value):
	return float(quantity) * float(value)