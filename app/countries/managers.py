from django.db import models
from django.db.models import Q


class CountrySearchManager(models.Manager):

    def search(self, **kwargs):
        qs = self.get_query_set()
        query = kwargs.get('query', '')
        government = kwargs.get('government', '')
        if government:
            qs = qs.filter(government_type=government)
        if query:
            qs = qs.filter(Q(Q(name__icontains=query) |
                Q(background__icontains=query)))
        return qs
