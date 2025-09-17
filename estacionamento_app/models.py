from django.db import models

from clientes.models import PessoaFisica
from funcionarios.models import Funcionario


class Estacionamento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=[('ocupado', 'Ocupado'), ('vago', 'Vago')])
    funcionario_responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.endereco} - {self.capacidade} vagas"

class VagaEstacionamento(models.Model):
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()

    def __str__(self):
        return f"Veiculo {self.veiculo.nome} em {self.estacionamento.nome}"

