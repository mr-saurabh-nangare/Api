from rest_framework import viewsets
from .models import Organizer,Event,Attendee
from .serializers import OrganizerSerializer,EventSerializer,AttendeeSerializer
# Create your views here.
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer