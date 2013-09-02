from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from haystack.views import SearchView, FacetedSearchView, search_view_factory
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet

from countries.forms import CountryHaystackForm


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view=TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'countries/', include('countries.urls')),
    url(r'search/', include('search.urls')),
    url(r'^haystack/basic/$', include('haystack.urls')),
    url(r'^haystack/custom/$', search_view_factory(
        view_class=SearchView,
        form_class=CountryHaystackForm
    ), name='custom_search'),
    url(r'^haystack/faceted/$', search_view_factory(
        searchqueryset=SearchQuerySet().facet('government'),
        view_class=FacetedSearchView,
        form_class=FacetedSearchForm
    ), name='faceted_search'),
)

urlpatterns += staticfiles_urlpatterns()
