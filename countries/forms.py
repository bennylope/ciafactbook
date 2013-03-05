from django import forms
from haystack.forms import SearchForm
from .models import Country


GOVERNMENT_CHOICES = [('', '')] + [
        (item.government_type, item.government_type) for
        item in Country.objects.all()]


class CountrySearchForm(forms.Form):
    """
    Basic form for searching with QuerySet filter method
    """
    q = forms.CharField(required=False)
    government = forms.ChoiceField(required=False, choices=GOVERNMENT_CHOICES)


class CountryHaystackForm(SearchForm):
    """
    Slightly customized search form that allows filtering on the SearchQuerySet
    """
    government = forms.ChoiceField(required=False, choices=GOVERNMENT_CHOICES)

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        query = self.cleaned_data.get('q', '')
        government = self.cleaned_data.get('government', '')
        sqs = self.searchqueryset

        if not query and not government:
            return self.no_query_found()

        if query:
            sqs = sqs.auto_query(query)

        if government:
            sqs = sqs.filter(government=government)

        if self.load_all:
            sqs = sqs.load_all()

        return sqs
