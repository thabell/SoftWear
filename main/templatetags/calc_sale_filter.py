from django import template
register = template.Library()
@register.filter
def calc_sale(cost, sale):
    return cost - (cost / 100 * sale)
