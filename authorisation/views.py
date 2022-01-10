import friendship
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from friendship.models import Friend

from authorisation.models import CustomPerson
from lobby.models import LobbyTask
from lobby.utils import leader_friends, user_friends


def my_view(request):
    # List of this user's friends
    all_friends = Friend.objects.friends(request.user)

    # List all unread friendship requests
    requests = Friend.objects.unread_requests(user=request.user)

    # List all rejected friendship requests
    rejects = Friend.objects.rejected_requests(user=request.user)

    ### Managing friendship relationships
    other_user = User.objects.get(pk=1)
    new_relationship = Friend.objects.add_friend(request.user, other_user)
    Friend.objects.are_friends(request.user, other_user)
    Friend.objects.remove_friend(other_user, request.user)

    # Can optionally save a message when creating friend requests
    some_other_user = User.objects.get(pk=2)
    message_relationship = Friend.objects.add_friend(
        from_user=request.user,
        to_user=some_other_user,
        message='Hi, I would like to be your friend',
    )

    # Attempting to create an already existing friendship will raise
    # `friendship.exceptions.AlreadyExistsError`, a subclass of
    # `django.db.IntegrityError`.
    dupe_relationship = Friend.objects.add_friend(request.user, other_user)
    AlreadyExistsError: u'Friendship already requested'


class LeaderBoard(TemplateView):
    template_name = 'leaderboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['leaderboard'] = LobbyTask.objects.all().values('id_Lobby__users__username').filter(isDone=True) \
            .annotate(total=Sum('points')).order_by('-total')
        print(context['leaderboard'])
        return context


class LeaderBoardFriends(TemplateView):
    template_name = 'leaderboard_friends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['leaderboard'] = LobbyTask.objects.all().values('id_Lobby__users__username').filter(isDone=True) \
            .annotate(total=Sum('points')).order_by('-total')

        context['friends'] = friendship.models.Friend.objects.all().values('to_user').filter(from_user_id=current_user)

        x = Friend.objects.all().filter(to_user_id=current_user.id)
        y= []
        for z in x:
            y.append(CustomPerson.objects.all().filter(id=z.from_user_id))
        contexthelp=[]

        def sort_fun(e):
            while True:
                try:
                    return e[0]['total']
                except:
                    return 0


        for z in y:
            contexthelp.append(LobbyTask.objects.all().filter(id_Lobby__users__username=z[0].username, isDone=True) \
                               .values('id_Lobby__users__username').annotate(total=Sum('points')).order_by('-total'))

        contexthelp.append(LobbyTask.objects.all().filter(id_Lobby__users__username=current_user, isDone=True) \
                           .values('id_Lobby__users__username').annotate(total=Sum('points')).order_by('-total'))
        print(contexthelp)

        contexthelp.sort(reverse= True, key=sort_fun)
        context['friends_points_data'] = contexthelp
        return context

class HomeView(TemplateView):  # noqa D101
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):  # noqa D102
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['users'] = CustomPerson.objects.filter(id=current_user.id).all()
        return context