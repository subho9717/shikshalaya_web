from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from shikshalaya_computer_app.models import Course,CustomUser,Student,Student_monthly_Fees
from django.contrib  import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'Hod/Home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    # session_year = Session_Year.objects.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        Class = request.POST.get('Class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile_number = request.POST.get('father_mobile_number')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile_number = request.POST.get('mother_mobile_number')
        present_address = request.POST.get('present_address')
        permenent_address = request.POST.get('permenent_address')
        course_id = request.POST.get('course_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_fees = request.POST.get('course_fees')
        # print(profile_pic,first_name,last_name,email,username,password,gender,date_of_birth,Class,joining_date,mobile_number,admission_number,father_name,father_occupation,father_mobile_number,mother_name,mother_mobile_number,mother_occupation,present_address,permenent_address,course_id,course,session_start,session_end,course_fees)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is alredy taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username is alredy taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            # session_year_start = Session_Year.session_start.objects.get(id = session_start)
            # session_year_end = Session_Year.session_end.objects.get(id = session_end)
            print(course)

            student = Student(
                admin = user,
                gender = gender,
                date_of_birth = date_of_birth,
                Class = Class,
                joining_date = joining_date,
                mobile_number = mobile_number,
                admission_number = admission_number,
                father_name=father_name,
                father_occupation = father_occupation,
                father_mobile = father_mobile_number,
                mother_name = mother_name,
                mother_occupation = mother_occupation,
                mother_mobile_number = mother_mobile_number,
                present_address = present_address,
                perment_address = permenent_address,
                course_id = course ,
                session_start = session_start,
                session_end = session_end,
                course_fees = course_fees
            )
            student.save()
            messages.success(request,user.first_name + '  ' + user.last_name + '   ' +"is successfully added")
            return redirect('add_student')

    context = {
        'course':course
    }
    return render(request,'Hod/add_student.html',context)


def VIEW_STUDENT(request):
    student  = Student.objects.all()
    context = {
        'student':student
    }
    return render(request,'Hod/view_student.html',context)


def Edit_STUDENT(request,id):
    student  = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student':student,
        'course':course
    }
    return render(request,'Hod/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        Class = request.POST.get('Class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile_number = request.POST.get('father_mobile_number')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile_number = request.POST.get('mother_mobile_number')
        present_address = request.POST.get('present_address')
        permenent_address = request.POST.get('permenent_address')
        course_id = request.POST.get('course_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_fees = request.POST.get('course_fees')


        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email =email
        user.username = username
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()

        student = Student.objects.get(admin = student_id)

        student.gender = gender
        student.date_of_birth = date_of_birth
        student.Class = Class
        student.joining_date = joining_date
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.father_name = father_name
        student.father_occupation = father_occupation
        student.father_mobile_number = father_mobile_number
        student.mother_name = mother_name
        student.mother_occupation = mother_occupation
        student.mother_mobile_number = mother_mobile_number
        student.present_address = present_address
        student.permenent_address = permenent_address
        student.session_start = session_start
        student.session_end = session_end
        student.course_fees = course_fees
        student.save()

        course  = Course.objects.get(id = course_id)
        student.course_id = course
        course.save()
        messages.success(request, 'All Record Updated Successfully')
        return redirect('view_student')
    return render(request,'Hod/edit_student.html')


def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id= admin)
    student.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_student')

def Detail_STUDENT(request,id):
    print(id)
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course
    }
    return render(request,'Hod/detail_student.html',context)



def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course  = Course(
            name = course_name
        )
        course.save()
        messages.success(request, 'Course Added Successfully')
        return redirect('add_course')
    return render(request,'Hod/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request,'Hod/view_course.html',context)


def Edit_COURCES(request,id):
    course = Course.objects.filter(id=id)
    context = {

        'course': course
    }
    return render(request,'Hod/edit_course.html',context)


def UPDATE_COURCES(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        print(course_id,course_name)
        course = Course.objects.get(id=course_id)
        course.name = course_name
        course.save()
        messages.success(request, 'All Record Updated Successfully')
        return redirect('view_course')
    return render(request,'Hod/edit_course.html')


def DELETE_COURCES(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_course')


def FEES_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course
    }

    return render(request,'Hod/fees_student.html', context)


def FEES_ADD_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        Class = request.POST.get('Class')
        course_id = request.POST.get('course_id')
        course_fees = request.POST.get('course_fees')
        months =  request.POST.get('months')
        month_fees = request.POST.get('month_fees')
        print(student_id,first_name,last_name,email,Class,course_id,course_fees,months,month_fees)


        Student_monthly_Fees_data = Student_monthly_Fees(
            Student_id=student_id,
            first_name = first_name,
            last_name = last_name,
            email = email,
            Class = Class,
            course = course_id,
            course_fees = course_fees,
            month = months,
            month_fees = month_fees
        )
        Student_monthly_Fees_data.save()
        messages.success(request, Student_monthly_Fees_data.first_name + '  ' + Student_monthly_Fees_data.last_name + '   ' + "fees collected")
        return redirect('fees_add_view_student')
    return render(request,'Hod/fees_view_student.html')


def FEES_ADD__VIEW_STUDENT(request):
    monthly_Fees = Student_monthly_Fees.objects.all()
    context={
        'monthly_Fees':monthly_Fees
    }
    return render(request,'Hod/fees_view_student.html',context)


def FEES_RECEIPT_STUDENT(request):
    return render(request,'Hod/fees_receipt.html')