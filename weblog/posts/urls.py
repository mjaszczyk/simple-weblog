from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.date_based import archive_year
from tagging.views import tagged_object_list
from weblog.posts.models import Post

BASE_POSTS_QS = Post.objects.all()

urlpatterns = patterns('',
    # Post detail URL
    url(r'post/([a-zA-Z0-9\-_]+),(?P<object_id>\d+)/$', object_detail,
        {'queryset': BASE_POSTS_QS}, name='posts.detail'),

    # Posts list by year
    url(r'archive/(?P<year>\d+)/$', archive_year, {'queryset': BASE_POSTS_QS,
        'make_object_list': True, 'date_field': 'create_time'}, name='posts.list.archive'),

    # Posts list by tag
    url(r'tag/(?P<tag>\w+)/$', tagged_object_list, {'queryset_or_model': BASE_POSTS_QS},
        name='posts.list.tag'),

    # Posts list
    url(r'$', object_list, {'queryset': BASE_POSTS_QS}, name='posts.list'),
)
