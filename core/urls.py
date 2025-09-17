# core/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoa/', views.pessoa, name='pessoa'),
    path('funcionarios/', include('funcionarios.urls')),  # Aqui é onde a URL da app funcionarios é incluída
]

