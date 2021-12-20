from urllib import request

import friendship.models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView, CreateView

import lobby
from authorisation.models import CustomPerson
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

    def form_valid(self, form):
        self.form=form
        current_user = self.request.user
        friends_add = self.form.cleaned_data['friends']
        pomoc = []
        print(friends_add)
        for x in range(len(friends_add)):
            y = CustomPerson.objects.filter(username = friends_add[x]).values_list('id',flat=True)[0]
            print(y)
            pomoc.append(y)
        print(pomoc)
        for lobby in Lobby.objects.filter(id=Lobby.objects.all().count()):
            lobby.users.add(current_user.id)
            for x in range(len(pomoc)):
                lobby.users.add(pomoc[x])

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
