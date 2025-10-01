from django.urls import path
from . import views
from .views import ClientesView, PessoasView, FuncionariosView, ClientesPFListView

# app_name = 'pessoas'

urlpatterns = [
    path('clientes/pj/cadastrar', views.ClientePJCreateView.as_view(), name='cliente_pj_cadastrar'),
    path('clientes/pf/cadastrar', views.ClientePFCreateView.as_view(), name='cliente_pf_cadastrar'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('funcionarios/', FuncionariosView.as_view(), name='funcionarios'),
    path('clientes_visualizar/', ClientesPFListView.as_view(), name='clientes_visualizar'),
]
