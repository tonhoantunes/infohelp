from django.db import models
from usuarios.models import User


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.TimeField(max_length=100)
    descricao = models.TextField(max_length=500)
    
    categoria_do_curso = {
        'Planilha': 'Planilha',
        'Texto': 'Texto',
        'Apresentação': 'Apresentação',
        'Design': 'Design',
    }

    nivel_do_curso = {
        ('Fácil', 'Fácil'),
        ('Médio', 'Médio'),
        ('Difícil', 'Difícil'),
    }


    categoria = models.CharField(max_length=100, choices=categoria_do_curso, blank=False)
    nivel = models.CharField(max_length=30, choices=nivel_do_curso, default="Fácil", blank=False)
    capa = models.ImageField(blank=True)

    def __str__(self):
        return self.nome
    
class Salvos(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salvos')
    cursos = models.ManyToManyField(Curso, related_name='salvos', blank=True)

    def __str__(self):
        return f'{self.nome} - {self.usuario.username}'


class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=400)
    capa = models.ImageField(blank=True)
    link = models.CharField(max_length=200)
    texto = models.TextField(max_length=2000, blank=True, null=True)  # Permite valores vazios
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    