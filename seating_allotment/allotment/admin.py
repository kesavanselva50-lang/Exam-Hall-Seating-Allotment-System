from django.contrib import admin
from .models import (
    Department,
    Student,
    Subject,
    Exam,
    ExamHall,
    SeatingAllotment
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'name', 'department', 'semester')
    list_filter = ('department', 'semester')
    search_fields = ('reg_no', 'name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name', 'department', 'semester')
    list_filter = ('department', 'semester')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'exam_date', 'session')
    list_filter = ('exam_date', 'session')


@admin.register(ExamHall)
class ExamHallAdmin(admin.ModelAdmin):
    list_display = ('hall_no', 'total_seats')
    search_fields = ('hall_no',)


@admin.register(SeatingAllotment)
class SeatingAllotmentAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'hall', 'seat_number')
    list_filter = ('exam', 'hall')
    search_fields = ('student__reg_no',)
