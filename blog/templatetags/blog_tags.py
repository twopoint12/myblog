from django import template
from ..models import Article, Category
from django.db.models import Count

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_category_count():
    return Article.objects.all().values('category_id').annotate(count=Count('category')).\
        values('category_id','category__name', 'count')