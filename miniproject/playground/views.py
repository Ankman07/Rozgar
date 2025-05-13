from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return render(request,'Login Page.html')
def dashboard(request):
    return render(request,'Dashboard.html')
def registration(request):
    return render(request, 'registration_portal.html')
def notification(request):
    return render(request,'Notification Panel.html')
def admin(request):
    return render(request,'Admin Panel.html')
# Create your views here.
