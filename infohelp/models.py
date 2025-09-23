from django.db import models
from usuarios.models import User
from django.core.exceptions import ValidationError



class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.TimeField(max_length=100)
    descricao = models.TextField(max_length=500)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    categoria_do_curso = [
        ('Planilha', 'Planilha'),
        ('Texto', 'Texto'),
        ('Apresentação', 'Apresentação'),
        ('Design', 'Design')
    ]

    nivel_do_curso = [
        ('Fácil', 'Fácil'),
        ('Médio', 'Médio'),
        ('Difícil', 'Difícil'),
    ]


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
    



class CursoProfessor(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cursos_professor")

    
    categoria_do_curso = [
        ('Planilha', 'Planilha'),
        ('Texto', 'Texto'),
        ('Apresentação', 'Apresentação'),
        ('Design', 'Design')
    ]

    imagem = models.ImageField(upload_to='cursos_professor/')

    #capa = models.ImageField(blank=True)

    categoria = models.CharField(max_length=100, choices=categoria_do_curso, blank=False)

    def __str__(self):
        return self.titulo
    
class AulaProfessor(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    curso = models.ForeignKey(CursoProfessor, on_delete=models.CASCADE, related_name="aulas")


    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    # Materiais didáticos
    video = models.FileField(upload_to="aulas/videos/", blank=True, null=True)
    pdf = models.FileField(upload_to="aulas/pdfs/", blank=True, null=True)
    ppt = models.FileField(upload_to="aulas/ppts/", blank=True, null=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def clean(self):
        # Restrições de formatos e tamanho
        if self.video and not self.video.name.endswith(".mp4"):
            raise ValidationError("O vídeo deve estar no formato MP4.")
        if self.video and self.video.size > 500 * 1024 * 1024:
            raise ValidationError("O vídeo não pode ultrapassar 500MB.")

        if self.pdf and not self.pdf.name.endswith(".pdf"):
            raise ValidationError("O PDF deve estar no formato PDF.")
        if self.pdf and self.pdf.size > 50 * 1024 * 1024:
            raise ValidationError("O PDF não pode ultrapassar 50MB.")

        if self.ppt and not (self.ppt.name.endswith(".ppt") or self.ppt.name.endswith(".pptx")):
            raise ValidationError("O arquivo deve estar no formato PPT ou PPTX.")

    def __str__(self):
        return f"{self.titulo} ({self.curso.titulo})"