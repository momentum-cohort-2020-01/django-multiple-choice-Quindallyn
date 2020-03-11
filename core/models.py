from django.db import models

class Flashcard(models.Model):
    side1 = models.TextField(max_length=None)
    side2 = models.TextField(max_length=None)
    # category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True)

class Deck(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

class Results(models.Model):
    pass