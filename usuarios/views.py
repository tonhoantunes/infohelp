from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CadastroForm

# Create your views here.
def login(request):
    
    return render(request, "login.html")

def cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        context = {
            'form': CadastroForm(),
        }

    return render(request, 'cadastro.html', context)
