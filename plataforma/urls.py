from django.urls import path

from . import views

urlpatterns = [
    path('plataforma/', views.plataforma, name="plataforma"),
    path('escolas/', views.escolas, name="escolas"),
    path('responsaveis/', views.responsaveis, name="responsaveis"),
    path('alunos/', views.alunos, name="alunos"),
    path('transportadores/', views.transportadores, name="transportadores"),

]