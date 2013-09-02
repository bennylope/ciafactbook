from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def query_update(context, field, value=''):
    """
    Replaces the given HTTP GET query paramter with the provided value.
    """
    params = context['request'].GET.copy()
    params[field] = value
    return params.urlencode()
