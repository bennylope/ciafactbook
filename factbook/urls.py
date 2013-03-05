from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from haystack.views import SearchView, search_view_factory
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet

from countries.forms import CountryHaystackForm


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view='countries.views.country_list', name='index'),
    url(r'countries/', include('countries.urls')),
    url(r'^haystack/default/$', include('haystack.urls')),
    url(r'^haystack/basic/$', search_view_factory(
        view_class=SearchView,
        form_class=ModelSearchForm
    ), name='basic_search'),
    url(r'^haystack/custom/$', search_view_factory(
        view_class=SearchView,
        form_class=CountryHaystackForm
    ), name='custom_search'),
)

urlpatterns += staticfiles_urlpatterns()

