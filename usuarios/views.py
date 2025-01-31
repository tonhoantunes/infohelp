from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CadastroForm

# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # Redirecione para a página inicial
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect("index")  # Redireciona para a página inicial após o cadastro
    else:
        form = CadastroForm()

    return render(request, "cadastro.html", {"form": form})
