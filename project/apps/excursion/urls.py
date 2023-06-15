from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("excursion_list/", views.ExcursionList.as_view(), name="excursion_list"),
    path("excursion_create/", staff_member_required(views.ExcursionCreate.as_view()), name="excursion_create"),
    path("excursion_delete/<int:pk>", staff_member_required(views.ExcursionDelete.as_view()), name="excursion_delete"),
    path("excursion_update/<int:pk>", staff_member_required(views.ExcursionUpdate.as_view()), name="excursion_update"),
    path("excursion/excursion_compra", views.crear_compra, name="excursion_compra"),
]