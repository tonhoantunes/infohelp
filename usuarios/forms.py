from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User, Perfil
import re

class CadastroForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        max_length=100,
        min_length=8,
        required=True,
        help_text="A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, um número e um caractere especial.",
    )
    confirm_password = forms.CharField(
        label="Confirme a senha",
        max_length=100,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isupper() for char in password):
            raise ValidationError("A senha deve ter pelo menos uma letra maiúscula.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("A senha deve ter pelo menos um número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("A senha deve ter pelo menos um caractere especial (!@#$%^&*).")

        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError({"confirm_password": "As senhas não coincidem."})

        return cleaned_data