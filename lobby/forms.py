from django import forms

from authorisation.models import CustomPerson
from .models import Rewards, Lobby
from .utils import validator_friends, user_friends


class BadgeForms(forms.ModelForm):
    description = forms.Textarea()

    class Meta:
        model = Rewards
        fields = ['image', 'name', 'description']


class LobbyCreate(forms.ModelForm):
    friends = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=validator_friends()
    )

    class Meta:
        model = Lobby
        fields = ['name', 'description', 'friends', 'time', 'type']
