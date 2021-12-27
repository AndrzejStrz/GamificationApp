from itertools import chain
from urllib import request

import friendship.models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

import lobby
from authorisation.models import CustomPerson
from lobby import models
from lobby.forms import LobbyCreate, TaskCreate
from lobby.models import Lobby, LobbyTask
from django.contrib.sessions.backends.db import SessionStore


class CreateLobby(CreateView):
    form_class = LobbyCreate
    template_name = 'lobbyCreate.html'
    success_url = '../SelectLobby'

    def form_valid(self, form):
        super().form_valid(form)
        self.form = form
        current_user = self.request.user
        friends_add = self.form.cleaned_data['friends']
        pomoc = []
        for x in range(len(friends_add)):
            y = CustomPerson.objects.filter(username=friends_add[x]).values_list('id', flat=True)[0]
            pomoc.append(y)
        for lobby in Lobby.objects.filter(id=Lobby.objects.all().count()):
            lobby.users.add(current_user.id)
            for x in range(len(pomoc)):
                lobby.users.add(pomoc[x])
        return super().form_valid(form)



class CreateTask(CreateView):
    form_class = TaskCreate
    template_name = 'addTask.html'
    success_url = '../SelectLobby/<int:id>'

    def form_valid(self, form):
        self.form = form

        full_path = self.request.get_full_path()
        reverse_path = full_path[::-1]
        id_from_path = reverse_path.split('/')[1]
        LobbyTask.objects.filter(id=LobbyTask.objects.last().id).update(id_Lobby=id_from_path)

        return super().form_valid(form)


def delete(request, id):
    obj = LobbyTask.objects.get(id=id)
    mydictionary = {
        "alltasks": LobbyTask.objects.all().filter(id_Lobby=obj.id).order_by('points')
    }
    sortdata(request)
    help = obj.id_Lobby.id
    obj.delete()
    return render(request, 'SelectLobby.html', context=mydictionary)


def sortdata(request):
    mydictionary = {
        "alltasks": LobbyTask.objects.all().order_by('points')
    }
    return render(request, 'allLobbyCreateTasks.html', context=mydictionary)


def edit(request,id):
    obj = LobbyTask.objects.get(id=id)
    mydictionary = {
        "id": id,
        "title": obj.title,
        "points": obj.points,
        "LevelOfDifficulty": obj.LevelOfDifficulty,
        "description": obj.description,
        "isDone": obj.isDone,
    }
    return render(request, 'editTask.html', context=mydictionary)


def update(request, id):
    obj = LobbyTask(id=id)
    print('asddsasda')
    obj.title = request.GET['title']
    obj.points = request.GET['points']
    obj.LevelOfDifficulty = request.GET['LevelOfDifficulty']
    obj.description = request.GET['description']
    obj.isDone = request.GET['isDone']
    obj.save()

    sortdata(request)
    mydictionary = {
        "alltasks": LobbyTask.objects.all()
    }
    return render(request, 'allLobbyCreateTasks.html', context=mydictionary)


class selectLobby(TemplateView):  # noqa D101
    template_name = 'selectLobby.html'

    def get_context_data(self, **kwargs):  # noqa D102
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['alllobbys']= Lobby.objects.filter(id__in=Lobby.objects.values_list('id', flat=True)).filter(
            users=current_user
        )

        return context

def take_id_from_path(full_path): # noqa D103
    reverse_path = full_path[::-1]
    right_id = reverse_path.split('/')
    return right_id[0]

class chosenLobby(TemplateView):
    template_name = 'allLobbyCreateTasks.html'

    def get_context_data(self, **kwargs):  # noqa D102
        context = super().get_context_data(**kwargs)
        full_path = self.request.get_full_path()
        id_path = take_id_from_path(full_path)
        context['alltasks']= LobbyTask.objects.filter(id_Lobby=id_path)

        return context