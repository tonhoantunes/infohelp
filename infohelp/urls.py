from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),    
    path('inicio/', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('busca/', views.busca, name="busca"),
    path('curso/', views.curso, name="curso"),
    path('perfil/', views.perfil, name="perfil"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
]