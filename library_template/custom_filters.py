from django import template

register = template.Library()

@register.filter
def lengthmatch(value, arg):
    if len(value) != len(arg):
        return []
    return zip(value, arg)