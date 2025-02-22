"""
URL configuration for employe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include    
    # Include the URL patterns for the employee app
from rest_framework.routers import DefaultRouter
from detail.views import DepartmentViewSet,EmployeeViewSet

print("DepartmentViewSet",DepartmentViewSet)
router = DefaultRouter()
router.register(r"department", DepartmentViewSet)
router.register(r"employee", EmployeeViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
