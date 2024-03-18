from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def loginUser(request):
    if request.method=="POST":
        id=request.POST.get('id')
        password_e=request.POST.get('password')
        user= authenticate(username=id,password=password_e)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
    #return HttpResponse("this is homepage")

def logoutUser(request):
    logout(request)
    return redirect('/login')
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")


