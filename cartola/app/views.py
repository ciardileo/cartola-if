"""
Arquivo que salva as views, funções que serão executadas quando certa url é acessada
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rich.console import Console

# console do rich text
console = Console()

# function-based-view
def home(request):
    console.log("Acessou página inicial")
    return render(  # renderiza um arquivo html para a view
		request, "index.html"
	)
  
def logout_view(request):
    console.log(f"Usuário {request.user.username} deslogado!")
    logout(request)
    return redirect("home")

# class-based-view, herda o CreateView para ter menos trabalho
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login') # retorna para o login depois de criar
