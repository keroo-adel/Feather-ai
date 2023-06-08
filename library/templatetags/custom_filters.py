from django import template

register = template.Library()

@register.filter
def split_string(value, delimiter):
    return value.split(delimiter)

@register.filter
def has_any(value, items):
    return any(item in value for item in items)
