from rest_framework import serializers
from .models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class meta:
        model = Employee
        fields = '__all__'