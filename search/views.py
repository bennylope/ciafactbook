from django.shortcuts import render
from django.template import RequestContext
from .forms import FactSearchForm


def search(request):
    """
    View function for searching all site content.

    The form class takes care of querying, filtering, and ordering.
    """
    form = FactSearchForm(request.GET)
    sq = form.search()
    sort = form.cleaned_data['sort']  # is_valid called by search method
    return render(request, "search/result_list.html",
            RequestContext(request, {"results": sq, 'form': form, 'sort': sort}))
