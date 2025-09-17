from django.db import models

from clientes.models import PessoaFisica


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)
    proprietario = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)

