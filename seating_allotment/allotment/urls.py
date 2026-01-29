from django.urls import path
from .views import login, staff

urlpatterns = [
        path('', login, name='login'),
        path('', staff, name='staff_login'),
    ]
