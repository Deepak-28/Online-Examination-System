from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Student, Staff , question_paper
import random
from . import Adminviews

def student_home(request):
    return render(request, 'Student/student_home.html')
    
def studentLoginPage(request):
    return render(request,"Student/student_login_page.html")
