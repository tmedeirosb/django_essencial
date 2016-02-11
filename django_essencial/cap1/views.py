from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from . import forms


# Create your views here.
def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height': 50})

    dados = {'nome': 'thiago medeiros', 'example': request.build_absolute_uri(example)}

    response = render(request,'cap1/index.html', dados)

    return response


def placeholder(request, width, height):
    form = forms.ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()

        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponse('tamanho inválido!')



