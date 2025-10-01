from django.contrib import messages
from django.core.paginator import Paginator

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import (
    PessoaFisicaForm, PessoaJuridicaForm,
    ClientePFInlineFormset, ClientePJInlineFormset
)
from .models import PessoaFisica, PessoaJuridica
from django.views.generic import TemplateView, ListView


class PessoasView(TemplateView):
    template_name = 'pessoas.html'

class ClientesView(TemplateView):
    template_name = 'clientes.html'

class FuncionariosView(TemplateView):
    template_name = 'funcionarios.html'

class ClientePFCreateView(TemplateResponseMixin, View):
    template_name = 'cliente_pf_form.html'

    def get_formset(self, data=None):
        return ClientePFInlineFormset(instance=self.pessoa, data=data)

    def get(self, request, *args, **kwargs):
        self.pessoa = PessoaFisica()
        form_pessoa = PessoaFisicaForm()
        formset = self.get_formset()
        return self.render_to_response({'form_pessoa': form_pessoa, 'formset': formset})

    def post(self, request, *args, **kwargs):
        self.pessoa = PessoaFisica()
        form_pessoa = PessoaFisicaForm(request.POST)
        formset = self.get_formset(data=request.POST)

        if form_pessoa.is_valid() and formset.is_valid():
            self.pessoa = form_pessoa.save()
            formset.instance = self.pessoa
            formset.save()
            return redirect('pessoas')
        return self.render_to_response({'form_pessoa': form_pessoa, 'formset': formset})

class ClientePJCreateView(TemplateResponseMixin, View):
    template_name = 'cliente_pj_form.html'

    def get_formset(self, data=None):
        return ClientePJInlineFormset(instance=self.pessoa, data=data)

    def get(self, request, *args, **kwargs):
        self.pessoa = PessoaJuridica()
        form_pessoa = PessoaJuridicaForm()
        formset = self.get_formset()
        return self.render_to_response({'form_pessoa': form_pessoa, 'formset': formset})

    def post(self, request, *args, **kwargs):
        self.pessoa = PessoaJuridica()
        form_pessoa = PessoaJuridicaForm(request.POST)
        formset = self.get_formset(data=request.POST)

        if form_pessoa.is_valid() and formset.is_valid():
            self.pessoa = form_pessoa.save()
            formset.instance = self.pessoa
            formset.save()
            return redirect('clientes:list')
        return self.render_to_response({'form_pessoa': form_pessoa, 'formset': formset})

class ClientesPFListView(ListView):
    model = PessoaFisica
    template_name = 'clientes_visualizar.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesPFListView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem clientes cadastrados!')
