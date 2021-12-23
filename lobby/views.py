from itertools import chain
from urllib import request

import friendship.models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

import lobby
from authorisation.models import CustomPerson
from lobby import models
from lobby.forms import LobbyCreate
from lobby.models import Lobby, LobbyTask, Lobby_Tasks


class CreateLobby(CreateView):
    form_class = LobbyCreate
    template_name = 'lobbyCreate.html'
    success_url = '../addTask'

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


def addTask(request):
    return render(request, 'addTask.html')

def addTaskSubmit(request):
    obj = LobbyTask()
    obj.title = request.GET['title']
    obj.points = request.GET['points']
    obj.LevelOfDifficulty = request.GET['LevelOfDifficulty']
    obj.description = request.GET['description']
    obj.save()


    Lobby_Tasks.objects.create(
        id_Lobby=Lobby.objects.get(id=Lobby.objects.all().count()),
        id_Task=LobbyTask.objects.get(id=obj.id)
    )


    mydictionary = {
        "alltasks": LobbyTask.objects.all()
    }
    return render(request, 'allLobbyCreateTasks.html', context=mydictionary)

def delete(request,id):
    obj= LobbyTask.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltasks": LobbyTask.objects.all().order_by('points')
    }
    sortdata(request)
    return render(request,'allLobbyCreateTasks.html', context=mydictionary)


def TasksList(request):
    x = Lobby.objects.all().filter(id=30)
    y = LobbyTask.objects.all().filter(id=78)
    z = Lobby_Tasks.objects.all().filter(id_Lobby=30).aggregate(Lobby.objects.filter(id=30))

    print(x)
    print(y)
    print(z)
    if (x and y) == Lobby_Tasks.objects.all().filter(id_Lobby=30,id_Task=78):
        print('gówno')
    mydictionary = {
        "alltasks": LobbyTask.objects.all().order_by('points')
    }

    sortdata(request)
    return render(request,'allLobbyCreateTasks.html', context=mydictionary)

def sortdata(request):
    mydictionary = {
        "alltasks": LobbyTask.objects.all().order_by('points')
    }
    return render(request,'allLobbyCreateTasks.html', context=mydictionary)

def edit(request, id):
    obj = LobbyTask.objects.get(id=id)
    mydictionary = {
        "title": obj.title,
        "points": obj.points,
        "LevelOfDifficulty": obj.LevelOfDifficulty,
        "description": obj.description,
        "isDone": obj.isDone,
        "id": obj.id
    }
    return render(request, 'editTask.html', context=mydictionary)

def update(request,id):
    obj = LobbyTask(id=id)
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
