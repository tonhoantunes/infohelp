from django.urls import path
from . import views

from usuarios.views import editar_perfil, perfil, alterar_senha

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
    path('curso/<int:curso_id>/aula/<int:aula_id>/editar', views.editar_aula, name="editar_aula"),


    path("listar_colecoes_salvos/", views.listar_colecoes_salvos, name="listar_colecoes_salvos"),
    path("criar_nova_colecao/", views.criar_nova_colecao, name="criar_nova_colecao"),
    path("salvar_curso/", views.salvar_curso_em_colecao, name="salvar_curso"),
    path("verificar_curso_salvo/<int:curso_id>/", views.verificar_curso_salvo, name="verificar_curso_salvo"),
    path("remover_curso_de_salvos/", views.remover_curso_de_salvos, name="remover_curso_de_salvos"),
    path('criar_salvos/', views.criar_salvos, name='criar_salvos'),


    path('biblioteca/', views.biblioteca, name="biblioteca"),

    path('busca/', views.busca, name="busca"),

    path('perfil/', perfil, name="perfil"),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),

    path('alterar_senha/', alterar_senha, name='alterar_senha'),



    path('professor/criar/curso/', views.criar_curso_professor, name="criar_curso_professor"),

    path("professor/cursos/", views.listar_cursos_professor, name="listar_cursos_professor"),

    # Cursos do professor
    path("professor/cursos/", views.detalhes_curso_professor, name="detalhes_curso_professor"),

    # Aulas do professor
    path("professor/curso/<int:curso_id>/aula/nova/", views.criar_aula_professor, name="criar_aula_professor"),
    path("professor/curso/<int:curso_id>/aula/<int:aula_id>/editar/", views.editar_aula_professor, name="editar_aula_professor"),
    path("professor/curso/<int:curso_id>/aula/<int:aula_id>/excluir/", views.excluir_aula_professor, name="excluir_aula_professor"),

]