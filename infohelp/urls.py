from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),    
    path('inicio/', views.inicio, name="inicio"),
    path('cursos/', views.listar_cursos, name="listar_cursos"),
    path('curso/novo/', views.criar_curso, name="criar_curso"),
    path('curso/<int:curso_id>/editar', views.editar_curso, name="editar_curso"),    
    path('curso/<int:curso_id>/', views.detalhes_curso, name="detalhes_curso"),
    path('curso/<int:curso_id>/excluir', views.excluir_curso, name="excluir_curso"),

    path('curso/<int:curso_id>/aula/<int:aula_id>/excluir', views.excluir_aula, name="excluir_aula"),

    path('curso/<int:curso_id>/aula/<int:aula_id>', views.detalhes_aula, name="detalhes_aula"),
    path('aula/nova/<int:curso_id>/', views.criar_aula, name="criar_aula"),

    path('aula/<int:curso_id>/<int:aula_id>/editar', views.editar_aula, name="editar_aula"),


    path('criar_salvos/', views.criar_salvos, name='criar_salvos'),

    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('busca/', views.busca, name="busca"),
    path('perfil/', views.perfil, name="perfil"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
]