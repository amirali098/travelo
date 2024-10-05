from django.utils import timezone

from django import template
from blog.models import Post,Category
register = template.Library()


@register.inclusion_tag("Blog/Module/popular_post.html")
def latest_posts():
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by("published_date")[:1]
    return {"posts":posts}


@register.inclusion_tag("Blog/Module/category.html")
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    value={}
    for name in categories:
        value[name]=posts.filter(category=name).count()
    print(value)
    return {"value":value}


@register.filter
def approved_comment_count(post):
    return post.comment_set.filter(approved=True).count()