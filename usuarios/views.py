from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CadastroForm, LoginForm, EditarPerfilForm

from django.contrib import messages

from .models import Perfil  # Importe o modelo Perfil
from django.contrib.auth.decorators import login_required, permission_required


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Cria um perfil para o usuário recém-criado
            Perfil.objects.create(usuario=user)

            # Loga o usuário automaticamente após o cadastro (opcional)
            # login(request, user)

            return redirect("inicio")
    else:
        form = CadastroForm()
    return render(request, "cadastro.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def perfil(request):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    return render(request, "perfil.html", {"perfil": perfil})

@login_required
def editar_perfil(request):
    # Obtém o perfil do usuário logado
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == "POST":
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("perfil") # Redireciona para a página inicial ou para a página de perfil
    else:
        form = EditarPerfilForm(instance=perfil)
    return render(request, "editar_perfil.html", {"form": form, "perfil" : perfil})
