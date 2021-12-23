from django.contrib import admin

from django.contrib import admin

from lobby.models import Lobby, Lobby_Tasks

from django.contrib import admin

from .models import LobbyTask


class LobbyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lobby, LobbyAdmin)

admin.site.register(LobbyTask)
admin.site.register(Lobby_Tasks)
