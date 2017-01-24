from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view='simplemooc.courses.views.index', name='index'),
    url(regex=r'^(?P<slug>[\w-]+)/$', view='simplemooc.courses.views.details',
        name='details'),
    url(regex=r'^(?P<slug>[\w-]+)/inscricao$', view='simplemooc.courses.views.enrollment', name='enrollment'),
    url(regex=r'^(?P<slug>[\w-]+)/cancelar-inscricao$', view='simplemooc.courses.views.undo_enrollment', name='undo_enrollment'),
    url(regex=r'^(?P<slug>[\w-]+)/anuncios$', view='simplemooc.courses.views.announcements', name='announcements'),
    url(regex=r'^(?P<slug>[\w-]+)/anuncios/(?P<pk>\d+)$', view='simplemooc.courses.views.show_announcement', name='show_announcement'),
    url(regex=r'^(?P<slug>[\w-]+)/lessons$', view='simplemooc.courses.views.lessons', name='lessons'),
    url(regex=r'^(?P<slug>[\w-]+)/lessons/(?P<pk>\d+)$', view='simplemooc.courses.views.lesson', name='lesson'),
    url(regex=r'^(?P<slug>[\w-]+)/materiais/(?P<pk>\d+)$', view='simplemooc.courses.views.material', name='material'),
]
