from django.shortcuts import render
# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):

    return render(request, "login.html")


def inicio(request):

    return render(request, "inicio.html")

def cursos(request):

    return render(request, "cursos.html")

def biblioteca(request):

    return render(request, "biblioteca.html")

def busca(request):

    return render(request, "busca.html")

def curso(request):

    return render(request, "pag_curso.html")

def perfil(request):

    return render(request, "perfil.html")