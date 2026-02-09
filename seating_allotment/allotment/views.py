from django.shortcuts import render, redirect
from .models import Exam, Student, ExamHall, SeatingAllotment, Department
from .utils import generate_auto_mixed_pg_seating
from django.shortcuts import get_object_or_404

def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'hall_count': ExamHall.objects.count(),
        'exam_count': Exam.objects.count(),
        'allotments': SeatingAllotment.objects.select_related(
            'student', 'exam', 'hall'
        )[:100],
    }
    return render(request, 'allotment/dashboard.html', context)


def generate_pg_mixed_allotments(request):
    # Clear previous allotments ONCE
    SeatingAllotment.objects.all().delete()

    exams = Exam.objects.order_by('exam_date', 'session')
    halls = list(ExamHall.objects.order_by('hall_no'))

    exam_groups = {}

    # Group exams by date + session
    for exam in exams:
        key = (exam.exam_date, exam.session)
        exam_groups.setdefault(key, []).append(exam)

    # Run seating per date + session
    for (exam_date, session), grouped_exams in exam_groups.items():
        generate_auto_mixed_pg_seating(grouped_exams, halls)

    return redirect('dashboard')







def student_page(request):
    students = Student.objects.all()
    departments = Department.objects.all()
    edit_student = None

    # ADD STUDENT
    if request.method == "POST" and "add_student" in request.POST:
        Student.objects.create(
            name=request.POST["name"],
            reg_no=request.POST["reg_no"],
            department_id=request.POST["department"],
            semester=request.POST["semester"]
        )
        return redirect("student_page")

    # UPDATE STUDENT
    if request.method == "POST" and "update_student" in request.POST:
        student = get_object_or_404(Student, id=request.POST["student_id"])
        student.name = request.POST["name"]
        student.reg_no = request.POST["reg_no"]
        student.department_id = request.POST["department"]
        student.semester = request.POST["semester"]
        student.save()
        return redirect("student_page")

    # LOAD EDIT DATA
    if request.GET.get("edit"):
        edit_student = get_object_or_404(Student, id=request.GET["edit"])

    # DELETE STUDENT
    if request.GET.get("delete"):
        Student.objects.filter(id=request.GET["delete"]).delete()
        return redirect("student_page")

    return render(request, "allotment/student_page.html", {
        "students": students,
        "departments": departments,
        "edit_student": edit_student
    })