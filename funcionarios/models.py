from django.db import models

from clientes.models import PessoaFisica


class Funcionario(PessoaFisica):
    tipoFuncionario = models.CharField(max_length=20)
    salario = models.FloatField()


