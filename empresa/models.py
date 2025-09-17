from django.db import models

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
        verbose_name_plural = 'Empresas'


