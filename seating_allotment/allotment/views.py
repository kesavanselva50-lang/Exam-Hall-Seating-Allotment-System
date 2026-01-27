from django.shortcuts import render

import random
from .models import Student, ExamHall, SeatingAllotment

def generate_seating_for_exam(exam):
   
    SeatingAllotment.objects.filter(exam=exam).delete()

   
    students = list(
        Student.objects.filter(
            department=exam.subject.department,
            semester=exam.subject.semester
        )
    )

    random.shuffle(students)

    halls = ExamHall.objects.all().order_by('hall_no')

    student_index = 0

    for hall in halls:
        for seat_no in range(1, hall.total_seats + 1):
            if student_index >= len(students):
                return  # All students allotted

            SeatingAllotment.objects.create(
                student=students[student_index],
                exam=exam,
                hall=hall,
                seat_number=seat_no
            )

            student_index += 1 