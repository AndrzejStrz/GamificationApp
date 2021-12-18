from django.contrib import admin

from django.contrib import admin

from lobby.models import Lobby


class LobbyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lobby, LobbyAdmin)