from django.contrib import admin

from . import models

admin.site.register(models.Excursion)
admin.site.register(models.FormaPago)
admin.site.register(models.Cliente)
admin.site.register(models.Comentario)