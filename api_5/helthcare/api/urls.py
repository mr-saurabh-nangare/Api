from django.urls import path
from .views import PatientList,DoctorList,AppointmentList
from django.http import JsonResponse
def api_root(request):
    return JsonResponse({
        "patients": "/api/patients/",
        "doctors": "/api/doctors/",
        "appointments": "/api/appointments/"
    })

urlpatterns=[
    path('', api_root, name='api-root'),
    path('patients/',PatientList.as_view(),name='patient_list'),
    path('doctors/',DoctorList.as_view(),name='doctor_list'),
    path('appointments/',AppointmentList.as_view(),name='appointment_list'),
]