from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import context
from . import forms, models
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def index(request):
    return render(request, "excursion/index.html")
    

class ExcursionList(ListView):
    model = models.Excursion
    template_name = "excursion/excursion_list.html"
    context_object_name = "excursiones"

class ExcursionCreate(CreateView):
    model = models.Excursion
    template_name = "excursion/excursion_create.html"
    form_class = forms.ExcursionForm
    success_url = reverse_lazy("excursion:index")

class ExcursionDelete(DeleteView):
    model = models.Excursion
    template_name="excursion/excursion_delete.html"
    success_url = reverse_lazy("excursion:excursion_list")


class ExcursionUpdate(UpdateView):
    model = models.Excursion
    form_class = forms.ExcursionForm
    template_name = "excursion/excursion_update.html"
    success_url = reverse_lazy("excursion:excursion_list")



def crear_compra(request):
    if request.method == "POST":
        form = forms.ExcursionVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("excursion:index")
    else:
        form = forms.ExcursionVentaForm()
    return render(request, "excursion/excursion_compra.html", {"form": form})
