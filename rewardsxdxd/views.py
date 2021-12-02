from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView, CreateView
from rewardsxdxd.forms import BadgeForms


class RewardsView(CreateView):
    form_class = BadgeForms
    template_name = 'rewards.html'
    success_url = '/'
