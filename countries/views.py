from django.shortcuts import render, get_object_or_404

from .models import Country
from .forms import CountrySearchForm


def country_list(request):
    countries = Country.objects.all()
    form = CountrySearchForm(request.GET or None)
    if form.is_valid():
        countries = Country.objects.search(**form.cleaned_data)
    return render(request, "countries/country_list.html",
            {"countries": countries, 'form': form})


def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, "countries/country_detail.html",
            {"country": country})
