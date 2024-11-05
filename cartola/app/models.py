"""
Arquivo que configura os modelos do banco de dados
"""

from django.db import models
from django.contrib.auth.models import User

class Jogador(models.Model):
    # info do jogador
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150, blank=True)
    posicao = models.CharField(max_length=50)
    foto = models.ImageField(blank=True, upload_to="jogadores/")
    
    # estatísticas 
    pontuacao_semanal = models.IntegerField(default=0)
    pontuacao_total = models.IntegerField(default=0)
    gols = models.IntegerField(default=0)
    defesas = models.IntegerField(default=0)
    assistencias = models.IntegerField(default=0)
    desarmes = models.IntegerField(default=0)
    
    # estatísticas
    vitorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    partidas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class UserTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jogadores = models.ManyToManyField(Jogador)
    pontuacao_total = models.IntegerField(default=0)

    def __str__(self):
        return f"Time do {self.user.username}"
