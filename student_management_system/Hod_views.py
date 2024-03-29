from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from shikshalaya_computer_app.models import Course,CustomUser,Student,Student_monthly_Fees,Computer_Course,Computer_Student,Computer_Student_monthly_Fees,Computer_Expenses
from django.contrib  import messages
import datetime
import sqlite3
import logging
import  psycopg2
import pandas as pd

logging.basicConfig(filename="shikshalaya.log" , level=logging.DEBUG ,format='%(levelname)s  %(asctime)s %(message)s')
conn = psycopg2.connect(
        host="satao.db.elephantsql.com",
        database="bhkpnqch",
        user="bhkpnqch",
        password="u5N4eHFTnwxRj9XhlTMPhqy3kudxnqR0")
cursor = conn.cursor()

@login_required(login_url='/')
def HOME(request):



    student_count = Student.objects.all().count()
    computer_student_count = Computer_Student.objects.all().count()

    mydate = datetime.datetime.now()
    month = mydate.strftime("%B")

    # expenses fees
    def exp():
        q1 = 'SELECT sum("Amount") FROM shikshalaya_computer_app_computer_expenses where month = '"'%s'"' group by month;'%month
        cursor.execute(q1)

        for r in cursor.fetchall():
            return r[0]

    Computer_expenses_sum = exp()


    # #monthly fees
    #
    def mf_data():
        cursor.execute("select month,sum(month_fees) as month_fees from shikshalaya_computer_app_computer_student_monthly_fees where month = '"+month+"' group by month")

        data = cursor.fetchall()
        for r in data:
            return r[1]
    Computer_monthly_fees_sum = mf_data()

    #
    def mf_all():
        mf_all = []
        cursor.execute("select month,sum(month_fees) as month_fees from shikshalaya_computer_app_computer_student_monthly_fees  group by month")

        data = cursor.fetchall()
        for r in data:
            mf_all.append([r[0],r[1],1])
        return mf_all

    Computer_monthly_fees_chart = mf_all()

    def ex_all():
        ex_all = []
        cursor.execute('select month,sum("Amount") as month_expenses from shikshalaya_computer_app_computer_expenses  group by month')

        data = cursor.fetchall()
        for r in data:
            ex_all.append([r[0],r[1]])
        return ex_all

    Computer_monthly_expenses_chart = ex_all()

    content = {
            'student_count':student_count,
            'computer_student_count':computer_student_count,
            'Computer_expenses_sum' : Computer_expenses_sum,
            'month':month,
            'Computer_monthly_fees_sum':Computer_monthly_fees_sum,
            'Computer_monthly_fees_chart':Computer_monthly_fees_chart,
            'Computer_monthly_expenses_chart':Computer_monthly_expenses_chart
        }
    return render(request,'Hod/Home.html',content)



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
        # father_name = request.POST.get('father_name')
        # father_occupation = request.POST.get('father_occupation')
        # father_mobile_number = request.POST.get('father_mobile_number')
        # mother_name = request.POST.get('mother_name')
        # mother_occupation = request.POST.get('mother_occupation')
        # mother_mobile_number = request.POST.get('mother_mobile_number')
        present_address = request.POST.get('present_address')
        # permenent_address = request.POST.get('permenent_address')
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
                # father_name=father_name,
                # father_occupation = father_occupation,
                # father_mobile = father_mobile_number,
                # mother_name = mother_name,
                # mother_occupation = mother_occupation,
                # mother_mobile_number = mother_mobile_number,
                present_address = present_address,
                # perment_address = permenent_address,
                course_stud = course ,
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

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student  = Student.objects.all()
    context = {
        'student':student
    }
    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
def Edit_STUDENT(request,id):
    student  = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student':student,
        'course':course
    }
    return render(request,'Hod/edit_student.html',context)

@login_required(login_url='/')
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
        print(course_id)


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


        course  = Course.objects.get(id = course_id)
        print(course)
        student.course_stud = course
        course.save()
        student.save()
        messages.success(request, 'All Record Updated Successfully')
        return redirect('view_student')
    return render(request,'Hod/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id= admin)
    student.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_student')


@login_required(login_url='/')
def Detail_STUDENT(request,id):
    print(id)
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course
    }
    return render(request,'Hod/detail_student.html',context)


@login_required(login_url='/')
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

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request,'Hod/view_course.html',context)

@login_required(login_url='/')
def Edit_COURCES(request,id):
    course = Course.objects.filter(id=id)
    context = {

        'course': course
    }
    return render(request,'Hod/edit_course.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
def DELETE_COURCES(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_course')

@login_required(login_url='/')
def FEES_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    context = {
        'student': student,
        'course': course
    }

    return render(request,'Hod/fees_student.html', context)

@login_required(login_url='/')
def FEES_ADD_STUDENT_d(request,id):
    if request.method == 'POST':
        student_id = id
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

@login_required(login_url='/')
def FEES_ADD__VIEW_STUDENT(request):
    monthly_Fees = Student_monthly_Fees.objects.all()
    # print(monthly_Fees.)

    context={
        'monthly_Fees':monthly_Fees
    }
    return render(request,'Hod/fees_view_student.html',context)

@login_required(login_url='/')
def FEES_RECEIPT_STUDENT(request,id):
    monthly_Fees = Student_monthly_Fees.objects.filter(id=id)
    context = {
        'monthly_Fees': monthly_Fees
    }
    return render(request,'Hod/fees_receipt.html',context)

@login_required(login_url='/')
def ADD_COMPUTER_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course  = Computer_Course(
            name = course_name
        )
        course.save()
        messages.success(request, 'Course Added Successfully')
        return redirect('add_computer_course')
    return render(request,'Hod/computer_course_add.html')

@login_required(login_url='/')
def VIEW_COMPUTER_COURSE(request):
    course = Computer_Course.objects.all()

    context = {
        'course': course
    }
    return render(request,'Hod/computer_course_view.html', context)

@login_required(login_url='/')
def UPDATE_COMPUTER_COURCES(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        print(course_id, course_name)
        course = Computer_Course.objects.get(id=course_id)
        course.name = course_name
        course.save()
        messages.success(request, 'All Record Updated Successfully')
        return redirect('view_computer_course')
    return render(request, 'Hod/computer_course_edit.html')

@login_required(login_url='/')
def DELETE_COMPUTER_COURCES(request,id):
    course = Computer_Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_computer_course')

@login_required(login_url='/')
def Edit_COMPUTER_COURCES(request,id):
    course = Computer_Course.objects.filter(id=id)
    context = {
        'course': course
    }
    return render(request, 'Hod/computer_course_edit.html', context)

@login_required(login_url='/')
def ADD_COMPUTER_STUDENT(request):
    course = Computer_Course.objects.all()
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
        # joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        # father_name = request.POST.get('father_name')
        # father_occupation = request.POST.get('father_occupation')
        # father_mobile_number = request.POST.get('father_mobile_number')
        # mother_name = request.POST.get('mother_name')
        # mother_occupation = request.POST.get('mother_occupation')
        # mother_mobile_number = request.POST.get('mother_mobile_number')
        # present_address = request.POST.get('present_address')
        # permenent_address = request.POST.get('permenent_address')
        course_id = request.POST.get('course_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        registration_fees = request.POST.get('registration_fees')
        course_fees = request.POST.get('course_fees')
        print(profile_pic,first_name,last_name,email,username,password,gender,date_of_birth,mobile_number,admission_number,course_id,course,session_start,session_end,course_fees)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is alredy taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'username is alredy taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Computer_Course.objects.get(id=course_id)
            # session_year_start = Session_Year.session_start.objects.get(id = session_start)
            # session_year_end = Session_Year.session_end.objects.get(id = session_end)
            print(course)
            mydate = datetime.datetime.now()
            student = Computer_Student(
                admin=user,
                gender=gender,
                date_of_birth=date_of_birth,
                # joining_date=joining_date,
                mobile_number=mobile_number,
                admission_number=admission_number,
                # father_name=father_name,
                # father_occupation=father_occupation,
                # father_mobile=father_mobile_number,
                # mother_name=mother_name,
                # mother_occupation=mother_occupation,
                # mother_mobile_number=mother_mobile_number,
                # present_address=present_address,
                # perment_address=permenent_address,
                course_comp=course,
                session_start=session_start,
                session_end=session_end,
                registration_fees = registration_fees,
                course_fees=course_fees,
                month = mydate.strftime("%B")
            )
            student.save()
            messages.success(request, user.first_name + '  ' + user.last_name + '   ' + "is successfully added")
            return redirect('add_computer_student')

    context = {
        'course': course
    }
    return render(request, 'Hod/computer_student_add.html', context)

@login_required(login_url='/')
def VIEW_COMPUTER_STUDENT(request):
    student = Computer_Student.objects.all()
    cursor.execute('select "Student_id", sum(month_fees) as sum_month_fees from shikshalaya_computer_app_computer_student_monthly_fees group by Student_id ')
    data_result_mf = []
    for r in cursor.fetchall():
        data_result_mf.append([int(r[0]), r[1]])
    print(data_result_mf)



    cursor.execute("select id, course_fees	 from shikshalaya_computer_app_computer_student")
    data_result_cf = cursor.fetchall()
    # print(data_result_cf)

    def rem(data_result_cf, data_result_mf):
        rem_fee = []
        for cf1 in data_result_cf:
            for mf1 in data_result_mf:

                if cf1[0] == mf1[0]:
                    # print(cf1[0] == mf1[0])
                    rem_fee.append([int(cf1[0]), int(cf1[1]) - int(mf1[1])])
        return rem_fee

    rem_fee = rem(data_result_cf, data_result_mf)
    print(rem_fee)


    context = {
        'student': student,
        'month_fees_cal': data_result_mf,
        'rem_fee':rem_fee
    }
    return render(request, 'Hod/computer_student_view.html', context)

@login_required(login_url='/')
def Edit_COMPUTER_STUDENT(request,id):
    student = Computer_Student.objects.filter(id=id)
    course = Computer_Course.objects.all()
    context = {
        'student': student,
        'course': course
    }
    return render(request, 'Hod/computer_student_edit.html', context)

@login_required(login_url='/')
def UPDATE_COMPUTER_STUDENT(request):
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
        registration_fees = request.POST.get('registration_fees')
        course_fees = request.POST.get('course_fees')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()

        student = Computer_Student.objects.get(admin=student_id)

        student.gender = gender
        student.date_of_birth = date_of_birth
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
        student.registration_fees = registration_fees
        student.course_fees = course_fees


        course = Computer_Course.objects.get(id=course_id)
        student.course_comp = course
        course.save()
        student.save()
        messages.success(request, 'All Record Updated Successfully')
        return redirect('view_computer_student')
    return render(request, 'Hod/computer_student_edit.html')

@login_required(login_url='/')
def DELETE_COMPUTER_STUDENT(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('view_computer_student')

@login_required(login_url='/')
def Detail_COMPUTER_STUDENT(request,id):
    student = Computer_Student.objects.filter(id=id)
    course = Computer_Course.objects.all()
    context = {
        'student': student,
        'course': course
    }
    return render(request, 'Hod/computer_student_detail.html', context)

@login_required(login_url='/')
def FEES_COMPUTER_STUDENT(request,id):
    student = Computer_Student.objects.filter(id=id)
    course = Computer_Course.objects.all()

    context = {
        'student': student,
        'course': course
    }

    return render(request, 'Hod/computer_student_fees.html', context)

@login_required(login_url='/')
def FEES_ADD_COMPUTER_STUDENT_d(request,id):
    if request.method == 'POST':
        student_id = id
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        course_id = request.POST.get('course_id')
        course_fees = request.POST.get('course_fees')
        months = request.POST.get('months')
        month_fees = request.POST.get('month_fees')
        # print(student_id, first_name, last_name, email,  course_id, course_fees, months, month_fees,'ok')

        Student_monthly_Fees_data = Computer_Student_monthly_Fees(
            Student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            course=course_id,
            course_fees=course_fees,
            month=months,
            month_fees=month_fees
        )
        Student_monthly_Fees_data.save()
        messages.success(request,Student_monthly_Fees_data.first_name + '  ' + Student_monthly_Fees_data.last_name + '   ' + "fees collected")
        return redirect('fees_add_view_computer_student')
    return render(request, 'Hod/computer_student_fees_view_student.html.html')

@login_required(login_url='/')
def FEES_ADD_VIEW_COMPUTER_STUDENT(request):
    print('test')
    monthly_Fees = Computer_Student_monthly_Fees.objects.all()
    context = {
        'monthly_Fees': monthly_Fees
    }

    return render(request, 'Hod/computer_student_fees_view_student.html', context)

@login_required(login_url='/')
def FEES_RECEIPT_COMPUTER_STUDENT(request,id):
    monthly_Fees = Computer_Student_monthly_Fees.objects.filter(id=id)
    context = {
        'monthly_Fees': monthly_Fees
    }
    return render(request, 'Hod/computer_student_fees_receipt.html', context)

@login_required(login_url='/')
def FEES_RECEIPT_COMPUTER_STUDENT_MONTH(request):
    student = Computer_Student.objects.all()
    monthly_Fees = Computer_Student_monthly_Fees.objects.all()
    context = {
        'student':student,
        'monthly_Fees': monthly_Fees
    }
    return render(request, 'Hod/student_fees_month_check.html', context)

@login_required(login_url='/')
def COMPUTER_EXPENSES_ADD(request):
    expenses = Computer_Expenses.objects.all()
    mydate = datetime.datetime.now()
    if request.method == 'POST':
        name = request.POST.get('name')
        # month = request.POST.get('month')
        Amount = request.POST.get('Amount')
        print()
        expenses = Computer_Expenses(
            name = name,
            month = mydate.strftime("%B"),
            Amount = Amount
        )
        expenses.save()
        messages.success(request, " Expenses is successfully added")
        return redirect('computer_expenses_view')
    context = {
        'expenses':expenses
    }
    return render(request, 'Hod/Computer_expenses_add.html',context)

@login_required(login_url='/')
def COMPUTER_EXPENSES_VIEW(request):
    expenses = Computer_Expenses.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, 'Hod/computer_expenses_view.html', context)

@login_required(login_url='/')
def COMPUTER_EXPENSES_DELETE(request,id):
    expenses = Computer_Expenses.objects.get(id=id)
    expenses.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('computer_expenses_view')

@login_required(login_url='/')
def COMPUTER_SALLARY(request):
    df = pd.read_sql_query(
        "select mf.month ,sum(mf.month_fees) as month_fees ,sum(cs.registration_fees) as registration_fees from shikshalaya_computer_app_computer_student_monthly_fees as mf inner join shikshalaya_computer_app_computer_student as cs on mf.month = cs.month group by mf.month, cs.month",
        conn)
    #
    ce = pd.read_sql_query('select month,sum("Amount") as expenses_amount from shikshalaya_computer_app_computer_expenses group by month',conn)
    fnl = df.merge(ce,how = 'inner',on='month')
    fnl['registration_fees_share'] = fnl['registration_fees']/2
    fnl['expenses_share'] = fnl['expenses_amount']/2
    fnl['employee_share'] = (fnl['month_fees']*55)/100
    fnl['rupam_subhajit_share'] = (fnl['month_fees']*55)/100 + fnl['registration_fees_share'] - fnl['expenses_share']
    fnl = round(fnl,1)
    for ms in fnl.itertuples():
            context = {
                    'month': ms[1],
                    'monthfees': str(ms[2]),
                    'regestraionfees': str(ms[3]),
                    'expenses': str(ms[4]),
                    'regfeesshare': str(ms[5]),
                    'expshare': str(ms[6]),
                    'employee': str(ms[7]),
                    'rupamsubhofinal': str(ms[8])}
            return render(request, 'Hod/shareview.html', context)