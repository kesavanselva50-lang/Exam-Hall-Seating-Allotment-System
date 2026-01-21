from django.contrib import admin
from .models import (
    Department,
    Student,
    Subject,
    Exam,
    ExamHall,
    SeatingAllotment
)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(ExamHall)
admin.site.register(SeatingAllotment)