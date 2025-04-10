from rest_framework import serializers
from .models import Team, Stadium, Event, Ticket
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    team_home = TeamSerializer()
    team_away = TeamSerializer()
    stadium = StadiumSerializer()

    class Meta:
        model = Event
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = Ticket
        fields = ['id', 'event', 'qr_code', 'is_used']

class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['event']