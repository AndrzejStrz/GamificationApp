from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from project import settings
from . import views
from .views import CreateLobby, selectLobby, chosenLobby, CreateTask, closeLobby, ListAchievementView

app_name = 'lobby'

urlpatterns = [
    path('lobbyCreate/', login_required(CreateLobby.as_view()), name='lobby'),
    path('SelectLobby/<int:id>/addTask', login_required(CreateTask.as_view()), name='addTask'),
    path('delete/<int:id>', login_required(views.delete), name='delete'),
    path('edit/<int:id>', login_required(views.edit), name='edit'),
    path('update/<int:id>', login_required(views.update), name='update'),
    path('SelectLobby', login_required(selectLobby.as_view()), name='SelectLobby'),
    path('SelectLobby/<int:id>', login_required(chosenLobby.as_view()), name='ChosenLobby'),
    path('SelectLobby/<int:id>/closeLobby', login_required(closeLobby.as_view()), name='ChosenLobby'),
    path('list', login_required(ListAchievementView.as_view()), name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)