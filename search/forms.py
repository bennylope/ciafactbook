from django import forms
from haystack.forms import SearchForm


class DummyPoint(object):
    """
    Satisfies the most basic needs of a Point object for the purpose of search
    distance without needing any of the GeoDjango dependencies.

    Haystack's `ensure_geometry` function simpy checks that the object has an
    attribute named `geom_type` which returns a string 'Point'. And for the
    purpose of getting the values the class needs a `get_coords` method.
    """
    points = ()
    geom_type = 'Point'

    def __init__(self, *args):
        self.points = args

    def __getitem__(self, index):
        return self.points[index]

    def get_coords(self):
        return self[0], self[1]


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
        center = DummyPoint(-87.627778,  41.881944)

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
