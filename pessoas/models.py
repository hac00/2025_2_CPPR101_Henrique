from django.db import models
from django.db.models.functions import Upper

from stdimage import StdImageField

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome completo')
    telefone = models.CharField('Telefone', max_length=15, help_text='Numero do telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='E-mail completo')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    foto = StdImageField('Foto', upload_to='pessoas', delete_orphans=True, null=True, blank=True)
    
    class Meta:
        abstract = True

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=14)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=14)

class Cliente(Pessoa):
    tipoCliente = models.CharField(max_length=20)
    # veiculos = models.ManyToManyField('Veiculo', related_name='clientes', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Funcionario(PessoaFisica):
    tipoFuncionario = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
    
