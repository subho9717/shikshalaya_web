"""student_management_system URL Configuration

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
from django.conf import settings
from  django.conf.urls.static import static
from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    # Login path
    path('',views.LOGIN,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),
    path('doLogout/',views.doLogout,name='logout'),
    #
    # progile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #hod panel
    path('Hod/Home',Hod_views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_views.Edit_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),
    path('Hod/Student/Detail/<str:id>',Hod_views.Detail_STUDENT,name='detail_student'),
    path('Hod/Student/Fees/<str:id>',Hod_views.FEES_STUDENT,name='fees_student'),
    path('Hod/Student/Fees_Add',Hod_views.FEES_ADD_STUDENT,name='fees_add_student'),
    path('Hod/Student/Fees_Add/View',Hod_views.FEES_ADD__VIEW_STUDENT,name='fees_add_view_student'),
    path('Hod/Student/Fees_Receipt/<str:id>',Hod_views.FEES_RECEIPT_STUDENT,name='fees_receipt_student'),

    path('Hod/Course/Add',Hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_views.Edit_COURCES,name='edit_course'),
    path('Hod/Course/Update',Hod_views.UPDATE_COURCES,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_views.DELETE_COURCES,name='delete_course'),


    path('Hod/Computer/Student/Add',Hod_views.ADD_COMPUTER_STUDENT,name='add_computer_student'),
    path('Hod/Computer/Student/View',Hod_views.VIEW_COMPUTER_STUDENT,name='view_computer_student'),
    path('Hod/Computer/Student/Edit/<str:id>',Hod_views.Edit_COMPUTER_STUDENT,name='edit_computer_student'),
    path('Hod/Computer/Student/Update',Hod_views.UPDATE_COMPUTER_STUDENT,name='update_computer_student'),
    path('Hod/Computer/Student/Delete/<str:admin>',Hod_views.DELETE_COMPUTER_STUDENT,name='delete_computer_student'),
    path('Hod/Computer/Student/Detail/<str:id>',Hod_views.Detail_COMPUTER_STUDENT,name='detail_computer_student'),
    path('Hod/Computer/Student/Fees/<str:id>',Hod_views.FEES_COMPUTER_STUDENT,name='fees_computer_student'),
    path('Hod/Computer/Student/Fees_Add_d/<str:id>',Hod_views.FEES_ADD_COMPUTER_STUDENT_d,name='fees_add_computer_student_d'),
    path('Hod/Computer/Student/Fees_Add/View',Hod_views.FEES_ADD_VIEW_COMPUTER_STUDENT,name='fees_add_view_computer_student'),
    path('Hod/Computer/Student/Fees_Receipt/<str:id>',Hod_views.FEES_RECEIPT_COMPUTER_STUDENT,name='fees_receipt_computer_student'),

    path('Hod/Computer/Course/Add',Hod_views.ADD_COMPUTER_COURSE,name='add_computer_course'),
    path('Hod/Computer/Course/View', Hod_views.VIEW_COMPUTER_COURSE, name='view_computer_course'),
    path('Hod/Computer/Course/Edit/<str:id>',Hod_views.Edit_COMPUTER_COURCES,name='edit_computer_course'),
    path('Hod/Computer/Course/Update',Hod_views.UPDATE_COMPUTER_COURCES,name='update_computer_course'),
    path('Hod/Computer/Course/Delete/<str:id>',Hod_views.DELETE_COMPUTER_COURCES,name='delete_computer_course'),



] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
