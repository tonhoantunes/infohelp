from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Aula
from .forms import CursoForm, AulaForm
# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):

    return render(request, "login.html")


def inicio(request):
    context = {
        "cursos" : Curso.objects.all()
    }

    return render(request, "inicio.html", context)




#CRUD de Cursos

def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(request, "listar_cursos.html", {'cursos': cursos})

def detalhes_curso(request, curso_id):
    context = {
        "curso": get_object_or_404(Curso, pk=curso_id)
    }

    return render(request, "pag_curso.html", context)

def criar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
        else:
            form = CursoForm()
    else:
        form = CursoForm()
    
    return render(request, "criar_curso.html", {'form': form})



def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    context = {
        "curso" : curso,
        "form" : CursoForm(instance=curso),
    }

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
        else:
            context["form"] = form
    
    return render(request, "editar_curso.html", context)



def excluir_curso(request, curso_id):
    context = {
        "curso": get_object_or_404(Curso, id=curso_id)
    }

    if request.method == "POST":
        context["curso"].delete()
        return redirect('listar_cursos')
    else:
        return render(request, "excluir_curso.html", context)

#CRUD de Aulas

def criar_aula(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            aula = form.save(commit=False)
            aula.curso = curso
            aula.save()
            return redirect('cursos.html', curso_id=curso.id)
    else:
        form = AulaForm()

    return render(request, 'criar_aula.html', {'form': form})




def biblioteca(request):

    return render(request, "biblioteca.html")

def busca(request):

    return render(request, "busca.html")

def perfil(request):

    return render(request, "perfil.html")

def editar_perfil(request):

    return render(request, "editar_perfil.html")