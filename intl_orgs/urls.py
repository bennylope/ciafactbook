from django.conf.urls import patterns, url

from .views import organization_list, organization_detail


urlpatterns = patterns('',
    url(r'^$', view=organization_list, name='organization_list'),
    url(r'^(?P<pk>\d+)/$', view=organization_detail, name='organization_detail'),
)
