from django.db import models

from veiculos.models import Veiculo
from estacionamento_app.models import Estacionamento
from pessoas.models import Funcionario

class VagaEstacionamento(models.Model):
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE, related_name='estadias')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='estadias')
    funcionario_entrada = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='estadias_entrada')
    funcionario_saida = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='estadias_saida')
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    valor_total = models.FloatField(default=0.0)

    def calcular_valor_total(self):
        if self.data_saida:
            duracao = (self.data_saida - self.data_entrada).total_seconds() / 3600
            self.valor_total = duracao * self.estacionamento.valor_hora
            self.save()
        return self.valor_total

    def __str__(self):
        return f"Veiculo {self.veiculo.nome} em {self.estacionamento.nome}"
