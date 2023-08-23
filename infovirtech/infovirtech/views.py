from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")
def home(request):
    return render(request, "index-2.html")

def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")