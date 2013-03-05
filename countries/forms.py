from django import forms

from .models import Country


GOVERNMENT_CHOICES = [('', '')] + [
        (item.government_type, item.government_type) for
        item in Country.objects.all()]


class CountrySearchForm(forms.Form):
    q = forms.CharField(required=False)
    government = forms.ChoiceField(required=False, choices=GOVERNMENT_CHOICES)
