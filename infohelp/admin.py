from django.contrib import admin
from .models import Curso, Salvos, Aula

admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Salvos)