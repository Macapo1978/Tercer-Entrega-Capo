from django import forms

from . import models


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = "__all__"