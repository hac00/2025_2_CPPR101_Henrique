from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import (
    PessoaFisicaForm, PessoaJuridicaForm,
    ClientePFInlineFormset, ClientePJInlineFormset
)
from .models import PessoaFisica, PessoaJuridica

class ClientePFCreateView(TemplateResponseMixin, View):
    template_name = 'clientes_pf_form.html'

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
            return redirect('clientes:list')
        return self.render_to_response({'form_pessoa': form_pessoa, 'formset': formset})

class ClientePJCreateView(TemplateResponseMixin, View):
    template_name = 'clientes_pj_form.html'

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
