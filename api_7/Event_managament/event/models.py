from django.db import models

# Create your models here.
class Organizer(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField(unique=True)
    phone = models.IntegerField(null=False)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location =  models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(Organizer,on_delete=models.CASCADE,related_name='events')
    def __str__(self):
        return self.title

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(null=False)
    event = models.ManyToManyField(Event,related_name='attendees')
    def __str__(self):
        return self.name