from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import staff, student, hostel, category, complaint
from django.contrib import messages
from datetime import datetime

# Create your views here
from django.db import transaction

def home(request):
    return render(request,'new_homepage.html')

def loginUser_asStudent(request):
    if request.method == "POST":
        username = request.POST.get('id')  # Assuming 'username' is the field for student_id or email
        password = request.POST.get('password')

        # Check if the user exists in the Student table
        try:
            student_object = student.objects.get(student_id=username)  # Assuming student_id is used as the username
        except student.DoesNotExist:
            student_object = None

        if student_object is not None:
            # Authenticate the user using the authenticate method
            #user = authenticate(username=student_object.student_id, password=student_object.password)
            if password==student_object.password:
                #messages.success(request, "Login successful")
                request.session['username'] = username
                return redirect('/lodgecomplaint')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/login')
        else:
            messages.error(request, "User does not exist")
            return redirect('/login')
    return render(request, 'login.html')

def loginUser_asStaff(request):
    if request.method == "POST":
        username = request.POST.get('id')  # Assuming 'username' is the field for student_id or email
        password = request.POST.get('password')

        # Check if the user exists in the Student table
        try:
            staff_object = staff.objects.get(staff_id=username)  # Assuming student_id is used as the username
        except staff.DoesNotExist:
            staff_object = None

        if staff_object is not None:
            # Authenticate the user using the authenticate method
            #user = authenticate(username=student_object.student_id, password=student_object.password)
            if password==staff_object.password:
                #messages.success(request, "Login successful")
                request.session['username'] = username
                return redirect('/checkcomplaint')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/login_staff')
        else:
            messages.error(request, "User does not exist")
            return redirect('/login_staff')
    return render(request, 'loginstaff.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
    #return HttpResponse("this is homepage")

def signup(request):
    if request.method == "POST":
        s = request.POST.get('id')
        f = request.POST.get('full_name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        pas = request.POST.get('password')
        h = request.POST.get('hostel')
        r = request.POST.get('roomno')

        # Save the form data to the database
        hostel_object = hostel.objects.get(hostel_id = h)
        sample=student.objects.create(student_id=s,full_name=f, email=e,phone=p, password=pas, hostel=hostel_object, room_no=r)
        sample2=sample
        sample2.is_active=True
        sample2.save()
        transaction.commit()
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
        c= request.POST.get('category')

         # Save the form data to the database
        category_object = category.objects.get(category_id = c)
        sample=staff.objects.create(staff_id=staff_id,full_name=full_name, email=email,phone=phone, password=password, category=category_object)
        sample2=sample
        sample2.is_active=True
        sample2.save()
        transaction.commit()
        messages.success(request,"Account created successfully, please login")
        return redirect('/login_staff')  # Redirect to a success page after successful signup
    return render(request, 'signup_staff.html')

def lodgecomplaint(request):
    username = request.session.get('username')
    student_object = student.objects.get(student_id = username)
    if request.method == 'POST':
        c_id = request.POST.get('category')
        describe = request.POST.get('complaint')

        category_object = category.objects.get(category_id = c_id)
        hostel_object = hostel.objects.get(hostel_id = 1)
        roomno=student_object.room_no
        #staff_object=staff.objects.get(staff_id=7)

        sample=complaint.objects.create(category=category_object,hostel=hostel_object, student=student_object, description=describe,room_no=roomno)
        sample.is_active=True
        if sample.staff is None:
            # Reload the complaint object from the database to fetch the updated staff_id
            #sample = complaint.objects.get(pk=sample.pk)
            #sample.save()
            sample.refresh_from_db()
        sample.save()

        #transaction.commit()
        return redirect('/lodgecomplaint')
    complaints=complaint.objects.filter(student_id=student_object)
    context={
                'name': student_object.full_name,
                'complaints': complaints,
            }
    return render(request,'student_dashboard.html',context)

def checkcomplaint(request):
    username = request.session.get('username')
    staff_object = staff.objects.get(staff_id = username)
    complaints=complaint.objects.filter(staff_id=staff_object)
    context={
                'name': staff_object.full_name,
                'complaints': complaints
            }
    return render(request,'staff_dashboard.html',context)


def studentacc(request):
    username = request.session.get('username')
    student_object = student.objects.get(student_id = username)
    context={
                'student': student_object
            }
    return render(request,'student_profile.html',context)


def staffacc(request):
    username = request.session.get('username')
    staff_object = staff.objects.get(staff_id = username)
    context={
                'staff': staff_object
            }
    return render(request,'staff_profile.html',context)


def updatestatus(request):
    c_id = request.GET.get('complaint_id')
    entry = get_object_or_404(complaint, pk=c_id)
    # Perform any additional logic or processing here
    entry.status=1
    entry.resolved_at = datetime.now()
    entry.save()

    staff_obj = staff.objects.get(staff_id = entry.staff.staff_id)
    staff_obj.count -= 1
    staff_obj.save()
    return redirect('/checkcomplaint')

def delete_by_student(request):
    c_id = request.GET.get('complaint_id')
    entry = get_object_or_404(complaint, pk=c_id)
    entry.delete_by_student = 1
    entry.save()
    return redirect('/lodgecomplaint')

def delete_by_staff(request):
    c_id = request.GET.get('complaint_id')
    entry = get_object_or_404(complaint, pk=c_id)
    entry.delete_by_staff = 1
    entry.save()
    return redirect('/checkcomplaint')

def edit_student(request):
    username = request.session.get('username')
    student_object = student.objects.get(student_id = username)
    context={
                'student': student_object
            }
    return render(request,'edit_student.html',context)

def update_student(request):
    username = request.session.get('username')
    student_object = student.objects.get(student_id = username)
    if request.method == "POST":
        f = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('contact')
        h = request.POST.get('hostel')
        r = request.POST.get('room')

        student_object.full_name=f
        student_object.email=e
        student_object.phone=p
        student_object.hostel=hostel.objects.get(hostel_id=h)
        student_object.room_no=r
        student_object.save()
    return redirect('/studentacc')

def edit_staff(request):
    username = request.session.get('username')
    staff_object = staff.objects.get(staff_id = username)
    context={
                'staff': staff_object
            }
    return render(request,'edit_staff.html',context)

def update_staff(request):
    username = request.session.get('username')
    staff_object = staff.objects.get(staff_id = username)
    if request.method == "POST":
        f = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('contact')

        staff_object.full_name=f
        staff_object.email=e
        staff_object.phone=p
        staff_object.save()
    return redirect('/staffacc')