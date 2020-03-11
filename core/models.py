from django.db import models
from users.models import User

class Flashcard(models.Model):
    side1 = models.TextField(max_length=None)
    side2 = models.TextField(max_length=None)
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)

class Deck(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Results(models.Model):
    pass