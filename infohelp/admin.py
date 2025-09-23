from django.contrib import admin
from .models import Curso, Salvos, Aula, CursoProfessor, AulaProfessor

admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Salvos)

admin.site.register(CursoProfessor)
admin.site.register(AulaProfessor)