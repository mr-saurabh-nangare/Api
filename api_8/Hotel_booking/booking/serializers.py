from rest_framework import serializers
from .models import Hotel,Room,Customer,Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    class Meta:
        model = Room
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    class Meta:
        model = Booking
        fields = '__all__'