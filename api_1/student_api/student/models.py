from django.db import models # type: ignore

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField (max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
