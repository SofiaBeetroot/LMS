import datetime
from django import template

register = template.Library()


@register.filter
def format_date(date: datetime.datetime) -> str:
    return date.strftime('%H:%M %d.%m.%Y')


@register.simple_tag(name='exists')
def get_object(topic):
    if topic:
        return topic.title
    else:
        return 'Ups...'


@register.filter(name='amount')
def get_comments_amount(comments):
    return comments.count()
