from django import forms
from haystack.forms import SearchForm
from haystack.utils.geo import Point


# GOVERNMENT_CHOICES = [('', '')] + [


class FactSearchForm(SearchForm):
    """
    Slightly customized search form that allows filtering on the SearchQuerySet
    """
    #government = forms.ChoiceField(required=False, choices=GOVERNMENT_CHOICES)
    sort = forms.ChoiceField(choices=(
                ('', 'relevance'),
                ('alpha', 'alpha'),
                ('distance', 'distance'),
                ('population', 'population')),
            required=False, widget=forms.HiddenInput)

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        query = self.cleaned_data.get('q', '')
        sqs = self.searchqueryset
        center = Point(-87.627778,  41.881944)

        if query:
            sqs = sqs.auto_query(query)

        if self.load_all:
            sqs = sqs.load_all()

        sort = self.cleaned_data.get('sort', '')
        if sort == 'alpha':
            return sqs.order_by('sort_name')
        elif sort == 'distance':
            return sqs.distance('location', center).order_by('distance')
        elif sort == 'population':
            return sqs.order_by('-population')

        return sqs
