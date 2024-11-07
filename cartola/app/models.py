"""
Arquivo que configura os modelos do banco de dados:
- Player;
- User;
- MatchDay;
- Teams;
- MatchDayPontuation;
"""

from django.db import models
from django.contrib.auth.models import User

# modelo do usuário
class UserProfile(models.Model):
    # info do usuário
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    total_best_user = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username


# modelo dos jogadores
class Player(models.Model):
    # info do jogador
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, upload_to="players/")
    
    # estatísticas
    total_points = models.IntegerField(default=0)
    total_goals = models.IntegerField(default=0)
    total_defenses = models.IntegerField(default=0)
    total_assists = models.IntegerField(default=0)
    total_tackles = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    total_losses = models.IntegerField(default=0)
    total_draws = models.IntegerField(default=0)
    total_matches = models.IntegerField(default=0)

    # determina o que será retornado quando a função é printada
    def __str__(self):
        return self.name
    
    
# modelo de um dia de jogo
class MatchDay(models.Model):
    # info do dia do jogo
    date = models.DateField()  
    best_player = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True, related_name="best_player")  
    best_user = models.ForeignKey("UserProfile", on_delete=models.SET_NULL, null=True, related_name="best_user") 

    def __str__(self):
        return f"Dia de jogo - {self.date}"


# pontuação de um jogador em um dia de jogo
class MatchDayPontuation(models.Model):
    # info
    match_day = models.ForeignKey("MatchDay", on_delete=models.CASCADE)  # referência ao dia do jogo
    player = models.ForeignKey("Player", on_delete=models.CASCADE)  # referência ao jogador

    # estatísticas do jogador nesse dia de jogo
    matches = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    defenses = models.IntegerField(default=0)
    tackles = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"Pontuação de {self.player.name} no dia {self.match_day.date}"


# escalação de um certo usuário em um dia de jogo
class Team(models.Model):
    # info
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="teams")  # related name é o nome que poderemos chamar todas as relações de Team com User
    match = models.ForeignKey(MatchDay, on_delete=models.CASCADE)  # Referência ao Dia de Jogo
    goleiro = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='goleiro')
    ala_esquerda = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='ala_esquerda')
    ala_direita = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='ala_direita')
    fixo = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='fixo')
    pivo = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='pivo')
    
    # pontuação
    pontuacao_total = models.IntegerField(default=0)

    def __str__(self):
        return f"Team de {self.user.username} para o jogo {self.match}"
