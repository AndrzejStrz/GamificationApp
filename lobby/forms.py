from django import forms

from .models import Lobby
from .utils import validator_friends


class LobbyCreate(forms.ModelForm):
    friends = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=validator_friends()
    )

    class Meta:
        model = Lobby
        fields = ['name', 'description', 'friends', 'time', 'type']


class AddTask(forms.ModelForm):
    LevelOfDifficulty = (('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'),)
    LevelOfDifficultyForm = forms.ChoiceField(required=True, choices=LevelOfDifficulty)


class IsDone(forms.ModelForm):
    isDone = (('True', 'True'), ('False', 'False'),)
    isDoneForm = forms.ChoiceField(required=True, choices=isDone)

