from django.shortcuts import render


def login(request):
    return render(request, 'allotment/login_page.html')
def staff(request):
    return render(request, 'allotment/staff_login.html')
