# funcionarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.funcionarios, name='funcionarios'),  # Essa é a URL que o link no template chama
]
