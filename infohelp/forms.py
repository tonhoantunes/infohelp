from django import forms
from django.core.exceptions import ValidationError
from .models import Curso, Salvos, Aula

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'carga_horaria', 'descricao', 'categoria', 'nivel', 'capa']

class SalvosForm(forms.ModelForm):
    class Meta:
        model = Salvos
        fields = ['nome']

    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # Preencher o formulário com a lista de músicas disponíveis
        # self.fields['cursos'].queryset = Curso.objects.all()

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = "__all__"
        exclude = ["curso"]