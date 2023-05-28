from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def index(request):
    return render(request,"comentario/index.html")

def crear_comentario(request):
    if request.method == "POST":
        form = forms.ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ComentarioForm()
    return render(request, "comentario/index.html", {"form": form})