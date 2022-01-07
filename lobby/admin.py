from lobby.models import Lobby, Achievement

from django.contrib import admin

from .models import LobbyTask


class LobbyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lobby, LobbyAdmin)
admin.site.register(LobbyTask)
admin.site.register(Achievement)
