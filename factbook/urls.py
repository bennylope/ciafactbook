from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view='countries.views.country_list', name='index'),
    url(r'countries/', include('countries.urls')),
    url(r'^haystack_default/', include('haystack.urls')),
)


urlpatterns += staticfiles_urlpatterns()

