from django.shortcuts import render
import json
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def login(request):
    return render(request, 'login.html')

def recycleCenter(request):
    return render(request, 'recycle_center.html')

def register(request):
    return render(request, 'register.html')

def report(request):
    return render(request, 'report.html')


