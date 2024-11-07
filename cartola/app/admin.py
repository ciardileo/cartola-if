"""
Arquivo da página de admin do Django

SuperUser do projeto:
ciardileo
leolopes.ciardi04@gmail.com
ciardi2233
"""

from django.contrib import admin
from .models import UserProfile, Player, Team, MatchDay, MatchDayPontuation

# registro dos modelos
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(MatchDay)
admin.site.register(MatchDayPontuation)