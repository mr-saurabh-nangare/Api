from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor =models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.date}"