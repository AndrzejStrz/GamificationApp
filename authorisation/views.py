from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from friendship.models import Friend

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