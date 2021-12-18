from datetime import timedelta
from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from authorisation.models import CustomPerson


class Rewards(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='achievement')


LevelOfDifficultly = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)


class Task(models.Model):
    points = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    LevelOfDifficulty = models.CharField(
        max_length=6,
        choices=LevelOfDifficultly)
    description = models.CharField(max_length=1000)


TypeOfLobby = (
    ('Race', 'Race'),
    ('Cooperation', 'Cooperation'),
)


class Lobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    time = models.DateTimeField(default=datetime.now() + timedelta(days=3), blank=True)
    users = models.ManyToManyField(CustomPerson)
    type = models.CharField(
        max_length=11,
        choices=TypeOfLobby)
    game_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def is_occupied(self):
        return self.users.count() >= 3

