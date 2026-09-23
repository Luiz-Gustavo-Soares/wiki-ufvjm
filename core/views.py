from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
            'paginas_recentes': [
                {'titulo': 'Laboratórios de SI', 'slug': 'laboratorios-de-si'},
                {'titulo': 'Guia do Calouro - Sistemas de Informação', 'slug': 'guia-calouro-si'},
                {'titulo': 'Como sobreviver a Buosi', 'slug': 'sobreviver-buosi'},
            ]
        }

    return render(request, 'core/home.html', context=context)


def sobre(request):
    return HttpResponse('Sobre a Wiki')

