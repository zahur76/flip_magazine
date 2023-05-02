from django.shortcuts import render, reverse, redirect
from magazines.forms import addMagazineForm
from django.contrib import messages

# Create your views here.
def add_magazine(request):
    """A view to add magazine"""

    if request.method=="POST":

        form = addMagazineForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Magazine Added!")
            return redirect(reverse("home"))

        messages.error(request, "Error Please Try Again!")
        return redirect(reverse("home"))
