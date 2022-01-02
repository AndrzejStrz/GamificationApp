from datetime import timedelta
from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from authorisation.models import CustomPerson


LevelOfDifficultly = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)


class Lobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    time = models.DateTimeField(default=datetime.now() + timedelta(days=3), blank=True)
    users = models.ManyToManyField(CustomPerson)

    def is_occupied(self):
        return self.users.count() >= 3


class LobbyTask(models.Model):
    title = models.CharField(max_length=100)
    points = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    LevelOfDifficulty = models.CharField(
        max_length=6,
        choices=LevelOfDifficultly)
    description = models.CharField(max_length=1000)
    isDone = models.BooleanField(default=False)
    id_Lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, related_name='id_Lobby',default=1)

    def __str__(self):
        return f'{self.title}'



class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    id_User = models.ForeignKey(CustomPerson, on_delete=models.CASCADE, related_name='id_User', default=1)

