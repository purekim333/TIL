from django.db import models

# Create your models here.
class GameSession(models.Model):
    target_number = models.IntegerField()
    user_guess = models.IntegerField(null=True)
    attempts = models.IntegerField(default=0)