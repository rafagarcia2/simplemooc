from django.conf.urls import url

urlpatterns = ['simplemooc.forum.views',
    url(r'^', 'index', name='index'),
]
