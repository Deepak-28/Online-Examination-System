"""onlineExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from examapp import views, Adminviews, staffviews, studentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('studentlogin_page',studentviews.studentLoginPage, name="studentlogin_page"), #STUDENT LOGIN PAGE
    path('stafflogin_page',staffviews.staffLoginPage, name="stafflogin_page"), #STAFF LOGIN PAGE
    path('doLogin',views.doLogin,name="do_login"), #LOGIN URL
    path('signup_student',views.signup_student,name="signup_student"), #STUDENT SIGNUP
    path('signup_staff',views.signup_staff,name="signup_staff"), #STAFF SIGNUP
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    path('logout_user', views.logout_user,name="logout"), #LOGOUT URL
    path('student_home', studentviews.student_home,name="student_home"), #STUDENT URL
    path('staff_home', staffviews.staff_home,name="staff_home"), #STAFF URL
    path('delete/<id>',Adminviews.delete,),

    path('check_email_exist', Adminviews.check_email_exist,name="check_email_exist"),
    path('check_username_exist', Adminviews.check_username_exist,name="check_username_exist"),
    path('add_student_form',Adminviews.add_student, name="add_student_form"),
    path('add_student_save',Adminviews.add_student_save, name="add_student_save"),

    path('exam_page',views.exam_view,name="exam_page"),

# ADMINVIEWS URLS
    path('signup_admin',views.signup_admin,name="signup_admin"), #ADMIN SIGNUP
    path('Adminlogin_page',Adminviews.AdminLoginPage,name="Admin_login_page"), #ADMIN LOGIN PAGE
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('admin_home', Adminviews.admin_home,name="admin_home"), #ADMIN HOME URL
    path('admin_staff_view',Adminviews.admin_staff_view, name='admin_staff_view'),
    path('admin_student_view', Adminviews.admin_student_view, name="admin_student_view"),
    path('question_upload', Adminviews.question_upload, name="question_upload"),
    path('question_paper_save', Adminviews.question_paper_save, name="question_paper_save"),

    
# STAFF URLS

]
