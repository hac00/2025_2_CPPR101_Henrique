from django import forms
from django.forms import ModelForm
from .models import PessoaFisica, PessoaJuridica, Cliente
from django.forms import inlineformset_factory

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ['nome', 'cpf', 'telefone', 'email']
        error_messages = {
            'nome': {'required': 'O nome é obrigatório.'},
            'cpf': {'required': 'O CPF é obrigatório.', 'invalid': 'CPF inválido.', 'unique': 'Este CPF já está cadastrado.'},
        }

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = ['cnpj', 'telefone', 'email']
        error_messages = {
            'cnpj': {'required': 'O CNPJ é obrigatório.', 'invalid': 'CNPJ inválido.', 'unique': 'Este CNPJ já está cadastrado.'},
        }

class ClientePFForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['pessoa_fisica']

class ClientePJForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['pessoa_juridica']

ClientePFInlineFormset = inlineformset_factory(
    PessoaFisica,
    Cliente,
    fk_name='pessoa_fisica',
    form=ClientePFForm,
    extra=1,
    can_delete=False
)

ClientePJInlineFormset = inlineformset_factory(
    PessoaJuridica,
    Cliente,
    fk_name='pessoa_juridica',
    form=ClientePJForm,
    extra=1,
    can_delete=False
)