from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import HttpResponse, render


# Create your views here.
@login_required(login_url='/auth/logar/')
def plataforma(request):
    return render(request, 'plataforma.html')


@login_required(login_url='/auth/logar/')
def escolas(request):
    return render(request, 'escolas.html')


@login_required(login_url='/auth/logar/')
def responsaveis(request):
    return render(request, 'responsaveis.html')


@login_required(login_url='/auth/logar/')
def transportadores(request):
    return render(request, 'transportadores.html')

@login_required(login_url='/auth/logar/')
def alunos(request):
    return render(request, 'alunos.html')

def external_page(request):
    return render(request, 'template_external.html')