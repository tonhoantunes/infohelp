from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User, Perfil

class CadastroForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
