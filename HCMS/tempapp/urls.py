"""
URL configuration for HCMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from tempapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login", views.loginUser_asStudent, name='login'),
    path("login_staff", views.loginUser_asStaff, name='login_staff'),
    path("logout",views.logoutUser,name="logout"),
    path("signup",views.signup,name="signup"),
    path("signupstaff",views.signupstaff,name="signupstaff"),
    path("updatestatus",views.updatestatus,name='updatestatus'),
    path("lodgecomplaint",views.lodgecomplaint,name="lodgecomplaint"),
    path("checkcomplaint",views.checkcomplaint,name="checkcomplaint"),
    path("studentacc", views.studentacc,name='studentacc'),
    path("staffacc", views.staffacc,name='staffacc'),
    path("delete_by_student", views.delete_by_student,name='delete_by_student'),
    path("delete_by_staff", views.delete_by_staff,name='delete_by_staff'),
    path("editstudent", views.edit_student,name='editstudent'),
    path("updatestudent", views.update_student,name='updatestudent'),
    path("editstaff", views.edit_staff,name='editstaff'),
    path("updatestaff", views.update_staff,name='updatestaff'),
    path("filter_complaints",views.filter_complaints,name='filter_complaints'),
]
