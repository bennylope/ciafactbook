from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'countries/', include('countries.urls')),
    url(r'^$', view='countries.views.country_list', name='index'),
)


urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#   )
