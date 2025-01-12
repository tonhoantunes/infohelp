from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.TimeField(max_length=100)
    descricao = models.TextField(max_length=500)
    categoria = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    capa = models.ImageField(blank=True)

    def __str__(self):
        return self.nome
    
class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    capa = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo