from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from authorisation.views import LeaderBoard, LeaderBoardFriends, HomeView
from project import settings


app_name = 'lobby'




urlpatterns = [
    path('leaderboard', login_required(LeaderBoard.as_view()), name='list'),
    path('leaderboard/friends', login_required(LeaderBoardFriends.as_view()), name='list'),
    path('',login_required(HomeView.as_view()), name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)