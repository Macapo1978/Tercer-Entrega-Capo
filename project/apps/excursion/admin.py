from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Excursion)
admin.site.register(models.FormaPago)
admin.site.register(models.Cliente)