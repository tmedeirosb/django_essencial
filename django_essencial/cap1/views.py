from django.shortcuts import render

# Create your views here.
def index(request):
    dados = {'nome': 'thiago medeiros'}

    response = render(request,'cap1/index.html', dados)

    return response
