from codecs import getencoder, getincrementalencoder
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import User,Staff,Student
from . import Adminviews 
# from examapp.EmailBackEnd import EmailBackEnd

# Create your views here.


def homepage(request):
    return render(request,"examapp/home.html")

# def ShowLoginPage(request):
#     return render(request,"examapp/login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    else:
        user=authenticate(request,username=request.POST.get("name"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect("admin_home")
            elif user.user_type=="2":
                return HttpResponseRedirect("staff_home")
            else:
                return HttpResponseRedirect("student_home")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect(reverse("Admin_login_page"))

            
# THIS IS HOME PAGE
# def admin_home(request):
#     return render(request, 'Admin/admin_home.html')

#THIS  IS FOR STUDENT HOME PAGE
# def student_home(request):
#     return render(request, 'Student/student_home.html')

# THIS IS FOR STAFF HOME PAGE
# def staff_home(request):
#     return render(request, 'Staff/staff_home.html')

# THIS IS FOR LOGOUT
def logout_user(request):
        logout(request)
        return HttpResponseRedirect("/")

# THIS IS FOR ADMIN SIGNUP
def signup_admin(request):
    return render(request,"Admin/admin_signup.html")

# THIS IS FOR STUDENT SIGNUP
def signup_student(request):
    return render(request,"Student/student_signup.html")

# THIS IS FOR STAFF SIGNUP
def signup_staff(request):
    return render(request,"Staff/staff_signup.html")


def do_admin_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")

    try:
        user=User.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        messages.success(request,"Successfully Created Admin")
        return HttpResponseRedirect(reverse("Admin_login_page"))
    except:
        messages.error(request,"Failed to Create Admin")
        return HttpResponseRedirect(reverse("Admin_login_page"))

def do_staff_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")

    try:
        user=User.objects.create_user(username=username,password=password,email=email,user_type=2)
        user.staff.address=address
        user.save()
        messages.success(request,"Successfully Created Staff")
        return render(request, 'Staff/staff_login_page.html')
    except:
        messages.error(request,"Failed to Create Staff")
        return redirect('stafflogin_page')

def do_signup_student(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")
    gender = request.POST.get("sex")
    section = request.POST.get("level")


    #try:
    user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                          first_name=first_name, user_type=3)
    user.student.address = address
    user.student.gender = gender
    user.student.section = section
    user.save()
    messages.success(request, "Successfully Added Student")
    return render(request, 'Student/student_login_page.html')


def exam_view(request):
    test1 = Adminviews.random_question(request)
    print(test1)
    return render(request,'examapp/exam_page.html',{'test':test1})


