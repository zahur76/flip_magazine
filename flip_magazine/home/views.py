from django.shortcuts import render
from magazines.forms import addMagazineForm


# Create your views here.
def index(request):
    """A view to return the index page"""

    form = addMagazineForm()

    context = {"form": form}

    return render(request, "home/index.html", context)
