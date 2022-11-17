from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'plataforma'

urlpatterns = [
    path('', views.plataforma, name="home"),
    path('escolas/', views.escolas, name="escolas"),
    path('responsaveis/', views.responsaveis, name="responsaveis"),
    path('alunos/', views.alunos, name="alunos"),
    path('transportadores/', views.transportadores, name="transportadores"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)