from django.contrib import admin

from .models import Country, InternationalOrganization


admin.site.register(Country)
admin.site.register(InternationalOrganization)
