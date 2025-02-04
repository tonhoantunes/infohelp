from django import forms
from django.core.exceptions import ValidationError
from .models import Curso, Aula

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'carga_horaria', 'descricao', 'categoria', 'nivel', 'capa']

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['titulo', 'descricao', 'capa', 'link', 'texto']