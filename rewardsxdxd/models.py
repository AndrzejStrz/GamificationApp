from django.db import models

class Rewards(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='achievement')
