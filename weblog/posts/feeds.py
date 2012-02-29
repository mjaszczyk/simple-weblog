from __future__ import absolute_import
from django.contrib.syndication.views import Feed
from django_markup.markup import formatter
from django.utils.html import strip_tags

from .models import Post


class PostsFeed(Feed):
    title = "Weblog posts"
    link = '/feed/'

    def items(self):
        return Post.objects.order_by('-create_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(formatter(item.content, filter_name='markdown'))
