from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OrganizerViewSet,EventViewSet,AttendeeViewSet

router = DefaultRouter()
router.register(r'organizers',OrganizerViewSet)
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]