from django.urls import path, include

from . import views
from .views import CreateLobby, selectLobby, chosenLobby, CreateTask

app_name = 'lobby'

urlpatterns = [
    path('lobbyCreate/', CreateLobby.as_view(), name='lobby'),
    path('SelectLobby/<int:id>/addTask', CreateTask.as_view(), name='addTask'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('SelectLobby', selectLobby.as_view(), name='SelectLobby'),
    path('SelectLobby/<int:id>', chosenLobby.as_view(), name='ChosenLobby'),
]