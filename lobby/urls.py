from django.urls import path, include

from . import views
from .views import CreateLobby
app_name = 'lobby'

urlpatterns = [
    path('lobbyCreate/', CreateLobby.as_view(), name='lobby'),
    path('addTask', views.addTask, name='addTask'),
    path('addTaskSubmit', views.addTaskSubmit, name='addTaskSubmit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('TasksList', views.TasksList, name='TasksList'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]