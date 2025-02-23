from rest_framework import serializers
from .models import Organizer,Event,Attendee

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    organizer = OrganizerSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Attendee
        fields ='__all__'