from django.shortcuts import render
from django.template import RequestContext
from .forms import FactSearchForm


def search(request):
    """
    """
    form = FactSearchForm(request.GET)
    sq = form.search()
    return render(request, "search/result_list.html",
            RequestContext(request, {"results": sq, 'form': form}))
