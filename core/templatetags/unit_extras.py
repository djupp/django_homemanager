from django import template

register = template.Library()


@register.simple_tag(name='unitconvert')
def unitconversion(amount, *args, **kwargs):
    curUnit = kwargs['current']
    newUnit = kwargs['new']
    return round(curUnit.convert_to(newUnit, amount), 1)
