from urllib import request

import friendship.models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView, CreateView

import lobby
from lobby import models
from lobby.forms import BadgeForms, LobbyCreate
from lobby.models import Lobby
from lobby.utils import validator_friends, user_friends


class RewardsView(CreateView):
    form_class = BadgeForms
    template_name = 'rewards.html'
    success_url = '/'


class CreateLobby(CreateView):
    form_class = LobbyCreate
    template_name = 'lobbyCreate.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        validator_friends()
        return super(CreateLobby, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.form=form
        current_user = self.request.user
        for lobby in Lobby.objects.filter(id=Lobby.objects.all().count()):
            lobby.users.add(current_user.id)
            friends = user_friends(current_user)
            for x in range(len(friends)):
                print(friends[x])
                lobby.users.add(friends[x])

        return super().form_valid(form)

def add_user_to_race_lobby(request, game_id):
    lobby = get_object_or_404(Lobby, game_id)
    if lobby.users.filter(pk=request.user.pk).exists():
        return redirect('game_page')
    elif not lobby.is_occupied():
        lobby.users.add(request.user)
        return redirect('game_page')
    else:
        return render(request, "error_page.html")
