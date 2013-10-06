from django.conf.urls import patterns, url

from readlingual.apps.reader import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^(?P<chapteroriginal_id>\d+)/(?P<chapter_id>\d+)/$', views.chapter, name='chapter'),
)
