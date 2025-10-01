# core/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', include('pessoas.urls')),
]

