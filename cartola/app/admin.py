"""
Arquivo da página de admin do Django
"""

from django.contrib import admin
from .models import Jogador, UserTeam

# registro dos modelos
admin.site.register(Jogador)
admin.site.register(UserTeam)