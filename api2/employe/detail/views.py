from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Employee
from .serializer import DepartmentSerializer,EmployeeSerializer

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer