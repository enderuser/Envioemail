from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def envia_email(request):
    send_mail('Assunto de teste', 'Este é o corpo do email para teste', 'wender@tisistema.com.br', ['kayky@tisistema.com.br'])
    return HttpResponse('Olá')