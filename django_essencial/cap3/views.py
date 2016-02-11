from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    dados = {'nome': 'Thiago Medeiros Barros'}
    response = render(request,'index.html', dados)

    return response