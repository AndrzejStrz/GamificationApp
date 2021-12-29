from django.conf.urls.static import static
from django.urls import path, include

from project import settings
from . import views
from .views import CreateLobby, selectLobby, chosenLobby, CreateTask, closeLobby, ListAchievementView

app_name = 'lobby'

urlpatterns = [
    path('lobbyCreate/', CreateLobby.as_view(), name='lobby'),
    path('SelectLobby/<int:id>/addTask', CreateTask.as_view(), name='addTask'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('SelectLobby', selectLobby.as_view(), name='SelectLobby'),
    path('SelectLobby/<int:id>', chosenLobby.as_view(), name='ChosenLobby'),
    path('SelectLobby/<int:id>/closeLobby', closeLobby.as_view(), name='ChosenLobby'),
    path('list', ListAchievementView.as_view(), name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)