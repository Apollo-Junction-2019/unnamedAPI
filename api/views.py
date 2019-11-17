from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework import viewsets
import json
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializer import *
from chatterbot import ChatBot
from scripts.bot import chatbot
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

class chatBotViewSet(View):
    chatterbot = chatbot
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body)

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
