from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/logar/')
def plataforma(request):
    return render(request, 'plataforma.html')