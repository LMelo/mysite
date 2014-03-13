from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns(
    '',
    # EXEMPLO 1
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    url(r'^$'),
    url(r'^(?P<pk>\d+)$'),
    url(r'^(?P<pk>\d+)/results/$'),
    url(r'^(?P<poll_id>\d+)/vote/$'),
)