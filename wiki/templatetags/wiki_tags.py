import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='render_markdown')
@stringfilter
def render_markdown(value):
    """onverte a string em Markdown para HTML"""
    
    # As extensões 'fenced_code' e 'tables' permitem blocos de código e tabelas
    return markdown.markdown(value, extensions=['fenced_code', 'tables'])