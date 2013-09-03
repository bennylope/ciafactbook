from haystack import indexes

from .models import InternationalOrganization


class OrgIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,
            template_name="search/indexes/intl_orgs/organization_text.txt")
    name = indexes.CharField(model_attr='name')
    sort_name = indexes.CharField(model_attr='name', indexed=False,
            stored=True)
    government = indexes.CharField(faceted=True)
    url = indexes.CharField(null=True, stored=True, indexed=False)
    population = indexes.IntegerField(null=True)

    def get_model(self):
        return InternationalOrganization

    def prepare(self, obj):
        """
        Downgrade the relevance of international organizations in search results.
        """
        return super(OrgIndex, self).prepare(obj)

    def prepare_government(self, obj):
        return u"international organization"

    def prepare_population(self, obj):
        """
        Returns the sum of all member nation populations
        """
        members = obj.members.all()
        if not members:
            return None
        return sum([member.population for member in members])

    def prepare_url(self, obj):
        return obj.get_absolute_url()
