from django import template

from eventlog.models import Log


register = template.Library()


class LogNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token):
        bits = token.split_contents()
        if len(bits) != 4:
            raise template.TemplateSyntaxError("Incorrect arguments for tag.")
        
        return cls(
            user = parser.compile_filter(bits[1]),
            as_var = bits[3]
        )
    
    def __init__(self, user, as_var):
        self.user = user
        self.as_var = as_var
    
    def render(self, context):
        user = self.user.resolve(context)
        
        user_qs = Event.objects.filter(context="user", user=user)
        user2_qs = Event.objects.filter(context="user2", user2=user)
        observer_qs = Event.objects.filter(context="observer", observer=user)
        
        context[self.as_var] = user_qs | user2_qs | observer_qs
        
        return ""


@register.tag
def user_event_log(parser, token):
    """
    Usage::
        {% user_event_log user as logs %}
    
    Sets a context variable that will be a queryset of event logs for the user.
    """
    return LogNode.handle_token(parser, token)
