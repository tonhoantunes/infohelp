from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Usuário"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Senha"})
    )

class CadastroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Senha"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Confirme a Senha"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "input", "placeholder": "Usuário"}),
            "email": forms.EmailInput(attrs={"class": "input", "placeholder": "E-mail"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "As senhas não coincidem.")

        return cleaned_data