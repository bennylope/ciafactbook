from django.shortcuts import render, get_object_or_404

from .models import InternationalOrganization


def organization_list(request):
    countries = InternationalOrganization.objects.all()
    return render(request, "intl_orgs/organization_list.html",
            {"countries": countries})


def organization_detail(request, pk):
    organization = get_object_or_404(InternationalOrganization, pk=pk)
    return render(request, "intl_orgs/organization_detail.html",
            {"organization": organization})
