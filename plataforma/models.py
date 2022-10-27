from django.db import models
from django.contrib.auth.models import User

from plataforma.views import responsaveis

# Create your models here.
class Plataforma(models.Model):
    choices_opcao = (('E', 'Escolas'),
                    ('R', 'Responsaveis'),
                    ('T', 'Transportadores'))
    opcao = models.CharField(max_length=1, choices=choices_opcao)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Escolas(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    responsavel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Responsaveis(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)

    def __str__(self):
        return self.nome


class Transportadores(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    veiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    capacidade = models.IntegerField()


    def __str__(self):
        return self.nome


class Alunos(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=16)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)
    responsaveis = models.ForeignKey(Responsaveis, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome