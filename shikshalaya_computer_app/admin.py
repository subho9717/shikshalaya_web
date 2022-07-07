from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Student_monthly_Fees)

admin.site.register(Computer_Course)
admin.site.register(Computer_Student)
admin.site.register(Computer_Student_monthly_Fees)

