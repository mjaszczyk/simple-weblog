from django.conf.urls import patterns, url


urlpatterns = patterns('weblog.posts.views',
    url(r'', 'index'),
)
