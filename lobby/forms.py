from django import forms

from authorisation.models import CustomPerson
from .models import Lobby, LobbyTask
from .utils import validator_friends


class LobbyCreate(forms.ModelForm):
    friends = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=validator_friends()
    )

    class Meta:
        model = Lobby
        fields = ['name', 'friends', 'description', 'time']


class TaskCreate(forms.ModelForm):
    class Meta:
        model = LobbyTask
        fields = ['title', 'points', 'LevelOfDifficulty', 'description']


class IsDone(forms.ModelForm):
    isDone = (('True', 'True'), ('False', 'False'),)
    isDoneForm = forms.ChoiceField(required=True, choices=isDone)


class selectLobby(forms.ModelForm):
    selectLobby = forms.ChoiceField(required=True,
                                    choices=Lobby.objects.filter(id__in=Lobby.objects.values_list('users', flat=True)))

    # use to fake when u migrate db
    # selectLobby = forms.ChoiceField(required=True, choices=(('True', 'True'), ('False', 'False'),))