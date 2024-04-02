from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import staff, student
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def loginUser_asStudent(request):
    if request.method=="POST":
        id=request.POST.get('id')
        password=request.POST.get('password')
        user= authenticate(request,username=id,password=password)
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
    #return HttpResponse("this is homepage")

def loginUser_asStaff(request):
    if request.method=="POST":
        id=request.POST.get('id')
        password_e=request.POST.get('password')
        user= authenticate(username=id,password=password_e)
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'loginstaff.html')
    return render(request, 'loginstaff.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
    #return HttpResponse("this is homepage")

def signup(request):
    if request.method == "POST":
        studentid = request.POST.get('id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        hostel = request.POST.get('hostel')
        roomno = request.POST.get('roomno')

        # Save the form data to the database
        sample=student(student_id=studentid,full_name=full_name, email=email,phone=phone, password=password, hostel=hostel, room_no=roomno)
        sample.save()
        messages.success(request,"Account created successfully, please login")
        return redirect('/login')  # Redirect to a success page after successful signup
    return render(request, 'signup_student.html')

def signupstaff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        category= request.POST.get('category')

         # Save the form data to the database
        sample=staff(staff_id=staff_id,full_name=full_name, email=email,phone=phone, password=password, category=category)
        sample.save()
        messages.success(request,"Account created successfully, please login")
        return redirect('/login_staff')  # Redirect to a success page after successful signup
    return render(request, 'signup_staff.html')
