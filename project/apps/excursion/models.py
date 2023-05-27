from django.db import models

# Create your models here.
class Excursion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    requisitos  = models.CharField(max_length=250)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class FormaPago(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apelido = models.CharField(max_length=150)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.CharField(max_length=250)
    excursion_comprada_id = models.ForeignKey(Excursion, on_delete=models.SET_NULL, null=True)
    formadepago_id = models.ForeignKey(FormaPago, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.apelido} {self.nombre}"



