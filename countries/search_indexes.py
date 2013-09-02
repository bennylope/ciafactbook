from haystack import indexes

from .models import Country


class CountryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,
            template_name="search/indexes/countries/country_text.txt")
    name = indexes.CharField(model_attr='name')
    sort_name = indexes.CharField(model_attr='name', indexed=False,
            stored=True)
    government = indexes.CharField(model_attr='government_type', faceted=True)
    population = indexes.IntegerField(model_attr='population')

    def get_model(self):
        return Country
