from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Student
from .serializer import CourseSerializer,StudentSerializer

# Create your views here.\
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer