from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from examapp.models import User ,Admin, Staff, Student, question_paper


class UserModel(UserAdmin):
    list_display = ('username','email','user_type','date_joined','last_login','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizotal = ()

admin.site.register(User,UserModel)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(question_paper)
