from django.db import models

# Create your models here.
class Comentario(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
   
 