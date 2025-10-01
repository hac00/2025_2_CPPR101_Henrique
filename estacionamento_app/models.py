from django.db import models

from pessoas.models import PessoaFisica
from pessoas.models import Funcionario


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Empresa')
    cnpj = models.CharField(max_length=14, help_text='CNPJ da Empresa', unique=True)
    endereco = models.CharField(max_length=200, help_text='Endereco da Empresa')
    receita_mensal = models.DecimalField(max_digits=10, decimal_places=2, help_text='Receita mensal da Empresa')
    despesa_mensal = models.DecimalField(max_digits=10, decimal_places=2, help_text='Despesa mensal da Empresa')

    def lucro_mensal(self):
        return self.receita_mensal - self.despesa_mensal

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Empresa'

class Estacionamento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()
    ocupadas = models.PositiveIntegerField(default=0)
    tipo = models.CharField(max_length=20, choices=[('ocupado', 'Ocupado'), ('vago', 'Vago')])
    funcionarios = models.ManyToManyField(Funcionario, related_name='estacionamentos', blank=True)
    valor_hora = models.FloatField(default=10.0)

    def __str__(self):
        return f"{self.nome} - {self.endereco}"
    
    def vagas_disponiveis(self):
        return self.capacidade - self.ocupadas
    
    def verificar_vaga(self):
        return self.vagas_disponiveis() > 0
    
    def ocupar_vaga(self):
        if self.verificar_vaga():
            self.ocupadas += 1
            self.save()
            return True
        return False
    
    def liberar_vaga(self):
        if self.ocupadas > 0:
            self.ocupadas -= 1
            self.save()
            return True
        return False

