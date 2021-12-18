from django.urls import path, include
from .views import RewardsView, CreateLobby

app_name = 'lobby'

urlpatterns = [
    path('rewards/', RewardsView.as_view(), name='rewards'),
    path('lobbyCreate/', CreateLobby.as_view(), name='lobby'),
]