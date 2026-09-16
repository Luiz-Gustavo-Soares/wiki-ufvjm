from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Bem Vindo a Wiki - UFVJM')


def sobre(request):
    return HttpResponse('Sobre a Wiki')

