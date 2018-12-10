from django import template
register = template.Library()

@register.simple_tag
def returnAdd(num1, num2):
    return int(num1) + int(num2)