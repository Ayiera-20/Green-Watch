from django.shortcuts import render
import json
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')


