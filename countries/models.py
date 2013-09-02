from django.db import models
from django.core.urlresolvers import reverse

from .managers import CountrySearchManager


class Country(models.Model):
    """
    A model for storing primary data about countries and country-level
    locations.
    """
    name = models.CharField(max_length=120)
    background = models.TextField()
    population = models.PositiveIntegerField(default=1)
    government_type = models.CharField(max_length=100, blank=True, null=True)
    lat = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)
    lng = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)

    objects = CountrySearchManager()

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __unicode__(self):
        return self.name

    def _get_location(self):
        if not self.lng and self.lat:
            return ()
        return self.lng, self.lat

    def _set_location(self, lng, lat):
        if not lng or not lat:
            raise AttributeError("Both latitude and longitude must be provided")
        self.lng, self.lat = lng, lat

    location = property(_get_location, _set_location)

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})
