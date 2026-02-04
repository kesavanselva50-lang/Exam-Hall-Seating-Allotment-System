from django.urls import path
from .views import dashboard, generate_all_allotments, student_page

urlpatterns = [
        path('', dashboard, name='dashboard'),
        path('generate-allotment/', generate_all_allotments, name='generate_allotment'),
        path("students/", student_page, name="student_page"),
        path("dashboard/", dashboard, name="dashboard"),
]
    
