import random
from itertools import cycle
from .models import Student, SeatingAllotment

def generate_auto_mixed_pg_seating(exams, halls):
    # delete previous allotments for these exams
    SeatingAllotment.objects.filter(exam__in=exams).delete()

    exam_students = {}

    for exam in exams:
        students = list(
            Student.objects.filter(
                department=exam.subject.department,
                semester=exam.subject.semester
            ).order_by('reg_no')
        )
        random.shuffle(students)
        exam_students[exam] = students

    hall_index = 0
    seat_no = 1
    exam_cycle = cycle(exams)

    while hall_index < len(halls):
        hall = halls[hall_index]
        exam = next(exam_cycle)

        if exam_students[exam]:
            student = exam_students[exam].pop(0)

            SeatingAllotment.objects.create(
                student=student,
                exam=exam,
                hall=hall,
                seat_number=seat_no
            )

            seat_no += 1

            if seat_no > hall.total_seats:
                hall_index += 1
                seat_no = 1

        if all(len(students) == 0 for students in exam_students.values()):
            break
