from django.conf.urls import patterns, url

from .views import country_list, country_detail


urlpatterns = patterns('',
    url(r'^$', view=country_list, name='country_list'),
    url(r'^(?P<pk>\d+)/$', view=country_detail, name='country_detail'),
)

