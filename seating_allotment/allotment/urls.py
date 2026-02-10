from django.urls import path
from .views import dashboard, staff_login, student_page, generate_pg_mixed_allotments

urlpatterns = [
        path('', dashboard, name='dashboard'),
        path('generate-allotment/', generate_pg_mixed_allotments, name='generate_pg_mixed_allotments'),
        path("students/", student_page, name="student_page"),
        path("staff-login/", staff_login, name="staff_login"),
        path("dashboard/", dashboard, name="dashboard"),
]
    
