from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def crear_compra(request):
    if request.method == "POST":
        form = forms.ExcursionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ExcursionForm()
    return render(request, "excursion/index.html", {"form": form})
