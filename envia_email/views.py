from django.shortcuts import render
from django.http import HttpResponse

def envia_email(request):
    return HttpResponse('Olá')