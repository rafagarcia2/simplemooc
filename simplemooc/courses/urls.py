from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view='simplemooc.courses.views.index', name='index'),
    url(regex=r'^(?P<slug>[\w-]+)/$', view='simplemooc.courses.views.details',
        name='details'),
]
