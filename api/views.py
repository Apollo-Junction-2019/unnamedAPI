from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializer import *

# Create your views here.
class chatAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answers to be viewed or edited
    """
    queryset = chatAnswers.objects.all()
    serializer_class = chatAnswersSerializer

class chatMessagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that displays all possible messages to send
    """
    queryset = chatMessages.objects.all()
    serializer_class = chatMessagesSerializer

class chatGamesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that is used to load the html/javascript game.
    """
    queryset = chatGames.objects.all()
    serializer_class = chatGamesSerializer

def home(request, template_name="example_app/templates/home.html"):
    context = {'title': 'Apollo Chatbot v1.0'}
    return render_to_response(template_name, context)