from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect
from enquiry.models import Enquiry
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url="/Login/")

def index(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('sub')
        msg=request.POST.get('msg')
        en=Enquiry(name=name,email=email,phone=phone,subject=subject,msg=msg)
        en.save()
        print(name,email,phone,subject,msg)
    return render(request, "index.html")

def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('sub')
        msg=request.POST.get('msg')
        en=Enquiry(name=name,email=email,phone=phone,subject=subject,msg=msg)
        en.save()
        print(name,email,phone,subject,msg)
    return render(request, "index-2.html")


def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")

def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('sub')
        msg=request.POST.get('msg')
        en=Enquiry(name=name,email=email,phone=phone,subject=subject,msg=msg)
        en.save()
        print(name,email,phone,subject,msg)
        return render(request, "index-2.html")
        
    return render(request, 'contacts.html')

def signup(request):
    if request.method =="POST":
        username=request.POST.get('username')
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(username,email,password)
        if User.objects.filter(username=username).exists():
            return render(request,"about.html")
        user_obj=User.objects.create(
            username=username,
            email=email)
        user_obj.set_password(password)
        user_obj.save()
        return render(request,'login.html')
    return render(request, "signup.html")

def logiN(request):
    if request.method == "POST" :
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        
        if not User.objects.filter(username=username).exists():
            return render(request,"signup.html")
        user_obj=authenticate(request,username=username,password=password)
        if user_obj:
            login(request,user_obj)
            return render(request,'logout.html')
    return render(request, "login.html")

def logouT(request):
    logout(request)
    
    return redirect('home/')
