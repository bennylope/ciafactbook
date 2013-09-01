from django.db import models
from django.core.urlresolvers import reverse


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

    def __unicode__(self):
        return self.name

    def _get_location(self):
        return self.lng, self.lat

    def _set_location(self, lng, lat):
        self.lng, self.lat = lng, lat

    location = property(_get_location, _set_location)

    def get_absolute_url(self):
        return reverse("intl_org_detail", kwargs={"pk": self.pk})
