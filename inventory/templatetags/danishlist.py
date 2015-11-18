from django import template

register = template.Library()

# FIXME: This filter is in fact not safe and should handle string escaping
@register.filter(is_safe=True)
def danishlist(l):
    cl = list(map(lambda x: str(x).capitalize(), l))
    if len(cl) == 0:
        ret = ""
    elif len(cl) == 1:
        ret = cl[0]
    elif len(cl) == 2:
        ret = cl[0] + " og " + cl[1]
    else:
        ret = ', '.join(cl[:-2]) + ", " + cl[-2] + " og " + cl[-1]
    return ret
