from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.reg_no} -{self.name}"
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
    
class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    session = models.CharField(
        max_length=10,
        choices=[('FN', 'Forenoon'), ('AN', 'Afternoon')]        
    )

    def __str__(self):
        return f"{self.subject.subject_name} - {self.exam_date}"
    
class ExamHall(models.Model):
    hall_no = models.IntegerField(unique=True)
    total_seats = models.IntegerField()

    def __str__(self):
        return f"Hall {self.hall_no}"


class SeatingAllotment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    hall = models.ForeignKey(ExamHall, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    class Meta:
        unique_together = ('exam', 'hall', 'seat_number')

    def __str__(self):
        return f"{self.student.reg_no} - {self.hall.hall_no} - Seat {self.seat_number}"