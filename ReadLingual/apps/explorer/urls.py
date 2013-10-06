from django.conf.urls import patterns, url

from readlingual.apps.explorer import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<work_id>\d+)/$', views.work, name='work'),
    url(r'^(?P<work_id>\d+)/(?P<worklanguage_id>\d+)/$', views.worklanguage, name='worklanguage'),
)
