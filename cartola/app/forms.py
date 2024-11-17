"""
modelos dos forms
"""

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# classe que gera um form de criação de usuários 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # garante que o username não está vazio antes de fazer a verificação
        if username and User.objects.filter(username=username).exists():
            raise ValidationError("Esse username já foi utilizado")

        return username  # retorna o username validado