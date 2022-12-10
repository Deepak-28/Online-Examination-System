from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Student, Staff

def staff_home(request):
    students = Student.objects.all()
    show = {'student':students}
    return render(request, 'Staff/staff_home.html',context=show)

def staffLoginPage(request):
    return render(request,"Staff/staff_login_page.html")



def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('staff_home')