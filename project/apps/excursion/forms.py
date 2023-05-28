from django import forms

from . import models


class ExcursionForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"