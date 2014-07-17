from django.conf.urls import patterns, include, url
from readlingual import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LangText.views.home', name='home'),
    # url(r'^LangText/', include('LangText.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^contact', TemplateView.as_view(template_name="contact.html")),
    url(r'^search', views.search, name='search'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^explorer/', include('readlingual.apps.explorer.urls')),
    url(r'^reader/', include('readlingual.apps.reader.urls')),
)
