from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    """Multiplies the value by the argument."""
    print("mul bro")
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0
