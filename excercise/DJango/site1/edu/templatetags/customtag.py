from django import template
register = template.Library()

@register.simple_tag
def returnAdd(num1, num2):
    return num1 + num2