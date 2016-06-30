from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view='simplemooc.core.views.home', name='home'),
    url(regex=r'^contato/$', view='simplemooc.core.views.contact',
        name='contact')
]
