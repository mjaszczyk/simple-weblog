from django.conf.urls import patterns, url
from django.views.generic.list_detail import object_list, object_detail
from weblog.posts.models import Post

urlpatterns = patterns('',
    url(r'post/(?P<object_id>\d+)/$', object_detail, {'queryset': Post.objects.all()}),
    url(r'page(?P<page>[0-9]+)/$', object_list, {'queryset': Post.objects.all()}),
    url(r'$', object_list, {'queryset': Post.objects.all()}),
)
