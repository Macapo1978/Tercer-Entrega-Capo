from django import forms

from . import models

class ExcursionForm(forms.ModelForm):
    class Meta:
        model = models.Excursion
        fields = "__all__"


class ExcursionVentaForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"