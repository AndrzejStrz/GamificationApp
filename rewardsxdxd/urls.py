from django.urls import path, include
from .views import RewardsView

app_name = 'rewardsxdxd'

urlpatterns = [
    path('rewards/', RewardsView.as_view(), name='rewardsxdxd')
]