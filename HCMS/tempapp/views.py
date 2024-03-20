from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Staff, Student

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
        password_e=request.POST.get('password')
        user= authenticate(username=id,password=password_e)
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
    if request.method == 'POST':
        studentid = request.POST['id']
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        hostel = request.POST['hostel']
        roomno = request.POST['roomno']

        # Save the form data to the database
        Student.objects.create(student_id=studentid,full_name=full_name, email=email,phone=phone, password=password, hostel=hostel, room_no=roomno)
        return redirect('/login')  # Redirect to a success page after successful signup
    return render(request, 'signup_student.html')

def signupstaff(request):
    if request.method == 'POST':
        staffid = request.POST['staffid']

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Save the form data to the database
        Staff.objects.create(username=username, email=email, password=password)
        return redirect('/login_staff')  # Redirect to a success page after successful signup
    return render(request, 'signup_staff.html')

