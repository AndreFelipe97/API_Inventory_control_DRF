from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    cod = models.IntegerField()
    razao = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=11)
    fone = models.CharField(max_length=11)
    public_place = models.CharField(max_length=100)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
