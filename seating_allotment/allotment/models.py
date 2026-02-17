from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# =====================================
# Department Model
# =====================================
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# =====================================
# Student Model
# =====================================
class Student(models.Model):
    SEMESTER_CHOICES = [(i, f"Semester {i}") for i in range(1, 9)]

    reg_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="students"
    )
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    class Meta:
        ordering = ["reg_no"]

    def __str__(self):
        return f"{self.reg_no} - {self.name}"


# =====================================
# Staff Model
# =====================================
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="staff_members"
    )

    def __str__(self):
        return self.user.username


# =====================================
# Subject Model
# =====================================
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField(choices=Student.SEMESTER_CHOICES)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    class Meta:
        ordering = ["subject_code"]

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"


# =====================================
# Exam Model
# =====================================
class Exam(models.Model):
    SESSION_CHOICES = [
        ('FN', 'Forenoon'),
        ('AN', 'Afternoon'),
    ]

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="exams"
    )
    exam_date = models.DateField()
    session = models.CharField(max_length=10, choices=SESSION_CHOICES)

    class Meta:
        unique_together = ('subject', 'exam_date', 'session')
        ordering = ["exam_date", "session"]

    def __str__(self):
        return f"{self.subject.subject_name} - {self.exam_date} ({self.session})"


# =====================================
# Building Model
# =====================================
class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# =====================================
# Exam Hall Model
# =====================================
class ExamHall(models.Model):
    hall_no = models.IntegerField(unique=True)
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="halls"
    )
    total_seats = models.PositiveIntegerField()

    class Meta:
        ordering = ["hall_no"]

    def __str__(self):
        return f"Hall {self.hall_no} ({self.building.name})"


# =====================================
# Seating Allotment Model
# =====================================
class SeatingAllotment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="allotments"
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="allotments"
    )
    hall = models.ForeignKey(
        ExamHall,
        on_delete=models.CASCADE,
        related_name="allotments"
    )
    seat_number = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('exam', 'hall', 'seat_number'),   # No duplicate seat in same exam
            ('student', 'exam'),               # One seat per student per exam
        )
        ordering = ["exam", "hall", "seat_number"]

    def clean(self):
        if self.seat_number > self.hall.total_seats:
            raise ValidationError("Seat number exceeds hall capacity.")

    def __str__(self):
        return f"{self.student.reg_no} - Hall {self.hall.hall_no} - Seat {self.seat_number}"
