from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
class Room(models.Model):
    ROOM_TYPES=(
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=8,decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        self.name
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    
    def __str__(self):
        return f"{self.customer.name} - {self.room}"