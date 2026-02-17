from .models import SeatingAllotment, Student


def generate_auto_mixed_pg_seating(exams, halls):

    # Delete previous allotments for these exams
    SeatingAllotment.objects.filter(exam__in=exams).delete()

    # Collect all students exam-wise in REG NO order
    combined_students = []

    for exam in exams:
        students = Student.objects.filter(
            department=exam.subject.department,
            semester=exam.subject.semester
        ).order_by('reg_no')  # 👈 VERY IMPORTANT

        for student in students:
            combined_students.append((student, exam))

    student_index = 0
    total_students = len(combined_students)

    # Fill halls one by one
    for hall in halls:

        for seat_no in range(1, hall.total_seats + 1):

            if student_index >= total_students:
                return  # All students allocated

            student, exam = combined_students[student_index]

            SeatingAllotment.objects.create(
                student=student,
                exam=exam,
                hall=hall,
                seat_number=seat_no
            )

            student_index += 1
