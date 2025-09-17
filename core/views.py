from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pessoa(request):
    return render(request, 'pessoa.html')
