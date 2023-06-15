from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.Excursion)
#admin.site.register(models.FormaPago)
#admin.site.register(models.Cliente)

@admin.register(models.Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion","requisitos","precio")
    list_filter = ("nombre","requisitos")
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ("nombre","precio")

@admin.register(models.FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    list_filter = ("nombre","descripcion")
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ("nombre","descripcion")

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apelido","mail")
    list_filter = ("nombre","apelido","mail")
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ("nombre","apelido","mail")