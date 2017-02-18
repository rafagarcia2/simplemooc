from django.conf.urls import url, patterns

urlpatterns = patterns('simplemooc.forum.views',
    url(r'^$', 'index', name='index'),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'index', name='index_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta$', 'reply_correct', name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta$', 'reply_incorrect', name='reply_incorrect'),
    url(r'^topico/(?P<slug>[\w-]+)/$', 'thread', name='thread'),
)
