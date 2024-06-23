# Import requied libraries to build template
from django import template


# Register a template to calculate subtotal
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
