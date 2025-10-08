from django.db import models
from django.db.models.functions import Upper

from stdimage import StdImageField

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome completo')
    telefone = models.CharField('Telefone', max_length=15, help_text='Numero do telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='E-mail completo')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.nome}: CPF: {self.cpf}'

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.nome}: CNPJ: {self.cnpj}'

class Cliente(Pessoa):
    TIPO_CHOICES = [('PF', 'Pessoa Física'),('PJ', 'Pessoa Juridica')]
    tipoCliente = models.CharField('Tipo', max_length=2, choices=TIPO_CHOICES)
    pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE, null=True, blank=True, related_name='clientes_pf')
    pessoa_juridica = models.ForeignKey(PessoaJuridica, on_delete=models.CASCADE, null=True, blank=True, related_name='clientes_pj')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = [Upper('nome')]

    def __str__(self):
        return super().nome
    #   return f'Cliente PF: {self.pessoa_fisica.nome}' if self.tipoCliente == 'PF' else f'Cliente PJ: {self.pessoa_juridica.nome}' # talvez?

''' # ajuda em algo isso ou nao?
    @property
    def nome(self):
        if self.tipoCliente == 'PF' and self.pessoa_fisica:
            return self.pessoa_fisica.nome
        elif self.tipoCliente == 'PJ' and self.pessoa_juridica:
            return self.pessoa_juridica.nome
        return 'Nome indefinido'
'''

class Funcionario(PessoaFisica):
    tipoFuncionario = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = StdImageField('Foto', upload_to='pessoas', delete_orphans=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = [Upper('nome')]

    def __str__(self):
        return super().nome
    
