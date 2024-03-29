from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT')
    )

    user_type =  models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender  = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100,default=0)
    admission_number = models.CharField(max_length=100,default=0)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100,default=0)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile_number = models.CharField(max_length=100,default=0)
    present_address = models.TextField()
    perment_address = models.TextField()
    course_stud = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_start = models.CharField(max_length=100)
    session_end =models.CharField(max_length=100)
    course_fees = models.CharField(max_length=100,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " First Name : "+self.admin.first_name + "  ,   " +"Last Name : "+ self.admin.last_name

class Student_monthly_Fees(models.Model):
    Student_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    course_fees = models.IntegerField(default=0)
    month = models.CharField(max_length=100)
    month_fees =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Computer_Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Computer_Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender  = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100,default=0)
    admission_number = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100,default=0)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile_number = models.CharField(max_length=100,default=0)
    present_address = models.TextField()
    perment_address = models.TextField()
    course_comp = models.ForeignKey(Computer_Course,on_delete=models.DO_NOTHING)
    session_start = models.CharField(max_length=100)
    session_end =models.CharField(max_length=100)
    registration_fees = models.IntegerField(default=0)
    course_fees = models.CharField(max_length=100,default=0)
    month = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " First Name : "+self.admin.first_name + "  ,   " +"Last Name : "+ self.admin.last_name

class Computer_Student_monthly_Fees(models.Model):
    Student_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    course_fees = models.IntegerField()
    month = models.CharField(max_length=100)
    month_fees =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Computer_Expenses(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    Amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)