from __future__ import absolute_import
from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.date_based import archive_year
from tagging.views import tagged_object_list

from .models import Post
from .feeds import PostsFeed


BASE_POSTS_QS = Post.objects.all()
PAGE_LIMIT = 10

urlpatterns = patterns('',
    
    # RSS feed
    url(r'^feed/$', PostsFeed(), name='posts.feed'),

    # Post detail URL
    url(r'^post/([a-zA-Z0-9\-_]+),(?P<object_id>\d+)/$', object_detail,
        {'queryset': BASE_POSTS_QS}, name='posts.detail'),

    # Posts list by year
    url(r'^archive/(?P<year>\d+)/$', archive_year, {'queryset': BASE_POSTS_QS,
        'make_object_list': True, 'date_field': 'create_time'},
        name='posts.list.archive'),

    # Posts list by tag
    url(r'^tag/(?P<tag>[^/]+)/$', tagged_object_list, {'paginate_by': PAGE_LIMIT,
        'queryset_or_model': BASE_POSTS_QS}, name='posts.list.tag'),

    # Posts list
    url(r'^$', object_list, {'paginate_by': PAGE_LIMIT, 'queryset': BASE_POSTS_QS}, name='posts.list'),
)
