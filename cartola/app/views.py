"""
Arquivo que salva as views, funções que serão executadas quando certa url é acessada
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rich.console import Console
from app.forms import RegisterForm
from django.contrib import messages

# console do rich text
console = Console()

# function-based-view
def home(request):
    console.log("Acessou página inicial")
    return render(  # renderiza um arquivo html para a view
		request, "index.html"
	)

# funções de login, logout e signup de usuários
def logout_view(request):
    console.log(f"Usuário {request.user.username} deslogado!")
    logout(request)
    return redirect("home")


def login_view(request):
    # verifica se ela será chamada como post (enviando o formulário) ou get (acessando a página)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logado com sucesso!")
            console.log(f"Usuário {user} logado com sucesso!")
            return redirect("home")
        else:
            console.log("ERRO! Verifique a senha e tente novamente!")
            messages.error(request, "ERRO! Verifique a senha e tente novamente!")
            
    context = {
        "form": AuthenticationForm()
    }
    
    return render(
        request, "user/login.html", context
    )
    
    
def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        console.log(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            console.log(f"Novo usuário {request.POST.get("username")} criado!")
            return redirect("login")
        else:                           
            console.log(f"Erro ao tentar criar usuário: {form.errors.as_text()}!")
            messages.error(request, f"ERRO! {form.errors.as_text()}")

    context = {
        'form': RegisterForm()
    }

    return render(
        request, 'user/signup.html', context
    )
