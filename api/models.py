from django.db import models

# Create your models here.


class DadosArduino(models.Model):
    nome = models.CharField(
        max_length=10,
    )
    sensor = models.CharField(
        max_length=10,
    )
