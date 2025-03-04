from rest_framework import serializers # type: ignore
from .models import Course,Student

class CourseSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"