from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet,RoomViewSet,CustomerViewSet,BookingViewSet

router = DefaultRouter()
router.register(r'hotels',HotelViewSet)
router.register(r'rooms',RoomViewSet)
router.register(r'customers',CustomerViewSet)
router.register(r'booking',BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]