from rest_framework import serializers
from api.models import *

class chatMessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = chatMessages
        fields = ('id', 'message')


class chatAnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = chatAnswers
        fields = ('answers', 'current_message', 'next_message')

class chatGamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = chatGames
        fields = ('id','game')