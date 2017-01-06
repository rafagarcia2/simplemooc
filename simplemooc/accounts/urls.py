from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'simplemooc.accounts.views.dashboard', name='dashboard'),
    url(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', 'simplemooc.accounts.views.register', name='register'),
    url(r'^editar/$', 'simplemooc.accounts.views.editar', name='editar'),
    url(r'^editar-password$', 'simplemooc.accounts.views.editar_password', name='editar_password'),
)
