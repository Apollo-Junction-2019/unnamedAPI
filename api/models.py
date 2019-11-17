from django.db import models
from jsonfield import JSONField
# Create your models here.

class chatMessages(models.Model):
    message = JSONField()

class chatAnswers(models.Model):

    answers = models.TextField()
    current_message = models.ForeignKey(chatMessages, on_delete=models.CASCADE, null=True, blank=True, related_name='current_message')
    next_message = models.ForeignKey('chatMessages', on_delete=models.CASCADE, null=True, blank=True, related_name='next_message')

class chatGames(models.Model):
    game =  models.TextField()
