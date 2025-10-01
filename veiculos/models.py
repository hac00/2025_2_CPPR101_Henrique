from django.db import models

from pessoas.models import Cliente

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

