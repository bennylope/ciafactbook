from django.db import models
from django.core.urlresolvers import reverse

from countries.models import Country


class InternationalOrganization(models.Model):
    """
    A model for storing data about international organizations like treaty
    alliances and international government.
    """
    name = models.CharField(max_length=120)
    description = models.TextField()
    lat = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)
    lng = models.DecimalField(blank=True, null=True, decimal_places=10,
            max_digits=13)
    members = models.ManyToManyField(Country, related_name="organizations")

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
        return reverse("organization_detail", kwargs={"pk": self.pk})
