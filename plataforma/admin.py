from django.contrib import admin
from . models import Alunos, Escolas, Responsaveis, Transportadores

admin.site.register(Alunos)
admin.site.register(Escolas)
admin.site.register(Responsaveis)
admin.site.register(Transportadores)

