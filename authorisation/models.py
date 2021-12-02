from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

class CustomPerson(AbstractUser):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    points = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

