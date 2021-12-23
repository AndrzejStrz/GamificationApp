import friendship
import friendship.models

from authorisation import models
from authorisation.models import CustomPerson
from lobby.models import Lobby


def validator_friends():
    uniqueFriendList = unique_freiends()

    for x in range(len(uniqueFriendList)):
        uniqueFriendList[x][0] = uniqueFriendList[x][1]
        uniqueFriendList[x] = tuple(uniqueFriendList[x])

    uniqueFriendList = tuple(uniqueFriendList)
    return uniqueFriendList

def user_friends(logged_user):
    table = unique_freiends()
    logged_user_friends = []

    for x in range(len(table)):
        if table[x][0] == logged_user.id:
            logged_user_friends.append(table[x][1])
        elif table[x][1] == logged_user.id:
            logged_user_friends.append(table[x][0])
    return logged_user_friends


def unique_freiends():
    friends = friendship.models.Friend.objects.all()
    friends_count = friends.count()
    friendsList = [[0 for x in range(2)] for y in range(friends.count())]

    for x in range(friends_count):
        friendsList[x][0] = friends[x].from_user.id
        friendsList[x][1] = friends[x].to_user.id
        friendsList[x].sort()
    uniqueFriendList = []
    for x in friendsList:
        if x not in uniqueFriendList:
            uniqueFriendList.append(x)

    for x in range(len(uniqueFriendList)):
        uniqueFriendList[x][0] = CustomPerson.objects.filter(id=uniqueFriendList[x][0])[0]
        uniqueFriendList[x][1] = CustomPerson.objects.filter(id=uniqueFriendList[x][1])[0]

    return uniqueFriendList

