from logging.config import valid_ident
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Admin, Staff,Student, User,question_paper
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddStudentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def AdminLoginPage(request):
    return render(request,"Admin/admin_login_page.html")

@login_required
def admin_home(request):
    staff_count = Staff.objects.all().count()
    student_count = Student.objects.all().count()
    question_count = question_paper.objects.all().count()
    return render(request, 'Admin/admin_home.html',{"staff_count":staff_count,"student_count":student_count,"question_count":question_count})

@login_required
def admin_staff_view(request):
    staffs=Staff.objects.all() 
    staff_name_list=[]
    for staff in staffs:
        staff_name_list.append(staff.admin.username)
   
    return render(request, 'Admin/admin_staff_view.html',{ 'staff_list':staffs})

@login_required
def admin_student_view(request):
    students=Student.objects.all()
    student_name_list=[]

    for student in students:
        student_name_list.append(student.admin.username)
    return render(request, 'Admin/admin_student_view.html', {'student_list':students})

@login_required
def delete(request, id):
    staff = User.objects.get(id=id)
    staff.delete()
    return redirect('admin_staff_view')

@login_required
def add_student(request):
    form=AddStudentForm()
    return render(request,"Admin/add_student_form.html",{"form":form})

@login_required
def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            gender=form.cleaned_data["gender"]
            section=form.cleaned_data["section"]

            try:
                user=User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.student.address=address
                user.student.gender=gender
                user.student.section=section
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student_form"))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse("add_student_form"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "Admin/add_student_form.html", {"form": form})
@login_required
def question_upload(request):
    return render(request, 'Admin/question_upload.html')


@login_required
def question_paper_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        question_name = request.POST.get("question_name")
        paper = request.POST.get("url")

        try:
            question = question_paper.objects.create(question_name=question_name,paper=paper)
            question.save
            messages.success(request,"Successfully Added")
            return HttpResponseRedirect(reverse("question_upload"))
        except:
            messages.error(request,"Failed to Create Admin")
            return HttpResponseRedirect(reverse("question_upload"))


@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=User.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=User.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)



# @login_required
# def random_question(request):
#     test = question_paper.objects.all()
#     paper_list = []
#     for i in test:
#         i= i.paper
#         paper_list.append(i)
#     print(paper_list)

#     mode = random.choice(paper_list)
#     print(mode)
#     # return mode
#     return render(request,'baseapp/admin_home.html',{'test':mode})

@login_required
def random_question(request):
    test = question_paper.objects.all()
    paper_list = []
    for i in test:
        i= i.paper
        paper_list.append(i)
    print(paper_list)

    mode = random.choice(paper_list)
    # print(mode)
    return mode 

