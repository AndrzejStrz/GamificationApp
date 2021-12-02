from django import forms
from .models import Rewards


class BadgeForms(forms.ModelForm):

    description= forms.Textarea()
    class Meta:
        model = Rewards
        fields = ['image', 'name', 'description']
