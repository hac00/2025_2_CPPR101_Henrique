from django.urls import path
from . import views

# app_name = 'pessoas'

urlpatterns = [
    path('clientes/pj/cadastrar', views.ClientePJCreateView.as_view(), name='clientes_pj_cadastrar'),
    path('clientes/pf/cadastrar', views.ClientePFCreateView.as_view(), name='clientes_pf_cadastrar'),
]
