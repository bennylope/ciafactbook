from django.db import models
from django.core.urlresolvers import reverse

from .managers import CountrySearchManager


class BasePlace(models.Model):
    name = models.CharField(max_length=120)
    background = models.TextField()
    lat = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)
    lng = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def _get_location(self):
        return self.lng, self.lat

    def _set_location(self, lng, lat):
        self.lng, self.lat = lng, lat

    location = property(_get_location, _set_location)


class Country(BasePlace):
    """
    A model for storing primary data about countries and country-level
    locations.
    """
    population = models.PositiveIntegerField(default=1)
    government_type = models.CharField(max_length=100, blank=True, null=True)

    objects = CountrySearchManager()

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})


class InternationalOrganization(BasePlace):
    """
    A model for storing data about international organizations like treaty
    alliances and international government.
    """
    members = models.ManyToManyField(Country)
