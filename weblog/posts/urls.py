from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_list, object_detail
from tagging.views import tagged_object_list
from weblog.posts.models import Post

urlpatterns = patterns('',
    # Post detail URL
    url(r'post/([a-zA-Z0-9\-_]+),(?P<object_id>\d+)/$', object_detail,
        {'queryset': Post.objects.all()}, name='posts.detail'),

    # Posts list by tag
    url(r'tag/(?P<tag>\w+)/$', tagged_object_list, {'queryset_or_model': Post.objects.all()},
        name='posts.list.tag'),

    # Posts list
    url(r'$', object_list, {'queryset': Post.objects.all()}, name='posts.list'),
)
