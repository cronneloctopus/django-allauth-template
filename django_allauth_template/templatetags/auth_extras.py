from django import template
register = template.Library()


@register.filter(name='dictKeyLookup')
def dictKeyLookup(the_dict, key):
    # Try to fetch from the dict, and if it's not found return an empty string.
    return the_dict.get(key, '')
