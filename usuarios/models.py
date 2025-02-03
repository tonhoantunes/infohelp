from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.usuario.username