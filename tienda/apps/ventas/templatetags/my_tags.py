from django import template

register = template.Library()

@register.inclusion_tag('ventas/tags/search_form.html')
def display_search_form():
	return {
		'buscar': context['buscar'],
	}