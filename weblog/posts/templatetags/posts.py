from __future__ import absolute_import
from django import template

from ..models import Post

register = template.Library()


@register.assignment_tag
def posts_archive_years(limit):
    return Post.objects.all().dates('create_time', 'year')[:limit]
