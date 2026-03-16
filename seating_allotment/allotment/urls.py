from django.urls import path
from .views import *
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),

    path('generate-allotment/', generate_pg_mixed_allotments, name='generate_allotment'),

    path("students/", student_page, name="student_page"),
    path("halls/", hall_page, name="hall_page"),
    path("subjects/", subjects_page, name="subjects"),
    path("subjects/delete/<int:pk>/", delete_subject, name="delete_subject"),
    path("departments/", departments_page, name="departments"),
    path("departments/delete/<int:pk>/", delete_department, name="delete_department"),
    path("master-upload/", master_upload, name="master_upload"),
    path("allotments/", seating_overview, name="seating_overview"),
    path('allotments/export-pdf/', export_master_pdf, name='export_master_pdf'),
    path("",staff_login, name="login"),
    path("logout/", staff_logout, name="logout"),
    path('staff-forgot/',staff_forgot, name='staff_forgot'),
    path('staff-register/',staff_register, name='staff_register'),
    path("download-template/",download_master_template, name="download_master_template"),


]
