from django import template

register = template.Library()

@register.tag
def vote_for_user(parser, token):
    """
    Retrieves the Vote by a user on a particular object
    For example::
    {% vote_by_user user on object as vote %}
    {{ vote }}
    
    """
    bits = list(token.split_contents())
    if len(bits) != 6 or bits[2] != "on" or bits[4] != "as":
        raise template.TemplateSyntaxError("%r expected format is 'user on object as name'" % bits[0])
    
    user    = bits[1]
    obj     = bits[3]
    name    = bits[5]
    
    return VoteForUserNode(user, obj, name)

