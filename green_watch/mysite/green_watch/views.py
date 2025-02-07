from django.shortcuts import render, redirect
from .models import Report
from .models import Contact
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def login_page(request):
    return render(request, 'login.html')

def recycleCenter(request):
    return render(request, 'recycle_center.html')

def register(request):
    return render(request, 'register.html')

def report(request):
    return render(request, 'report.html')


def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if full_name and email and password:
            user = CustomUser.objects.create_user(full_name=full_name, email=email, password=password)
            return redirect('login')  
        else:
            error_message = "Please fill in all fields"
            return render(request, 'register.html', {'error_message': error_message})
    
    return render(request, 'register.html')

def sign_in_submit(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('home')  
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    next_url = request.GET.get('next', '') 
    return render(request, 'login.html', {'next': next_url})




def logout_view(request):
    logout(request)  
    messages.success(request, "Logged out successfully")  
    return redirect('login')


@login_required(login_url='login')
def submit_report(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        community_name = request.POST.get('community_name')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        # Validation check
        if not location or not community_name or not description:
            # Return the form with an error message if any field is missing
            return render(request, 'report.html', {
                'error': 'Please fill all the required fields!'
            })

        # Create a new report and save it to the database
        try:
            Report.objects.create(
                location=location,
                community_name=community_name,
                description=description,
                photo=photo,
                user=request.user
            )
            messages.success(request, 'Your report has been submitted successfully!')
            return redirect('home')  
        except Exception as e:
            return render(request, 'report.html', {
                'error': f'An error occurred: {e}'
            })

    # If GET request, render the form
    return render(request, 'report.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validation check
        if not name or not email or not message:
            # Return the form with an error message if any field is missing
            return render(request, 'contact.html', {
                'error': 'Please fill all the required fields!'
            })

        # Optional: Add email format validation
        if not validate_email(email):
            return render(request, 'contact.html', {
                'error': 'Please enter a valid email address!'
            })
        
        user = request.user if request.user.is_authenticated else None

        try:
            Contact.objects.create(
                name=name,
                email=email,
                message=message,
                user=user
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  
        except Exception as e:
            return render(request, 'contact.html', {
                'error': f'An error occurred: {e}'
            })

    # If GET request, render the form
    return render(request, 'contact.html')

def validate_email(email):
    from django.core.exceptions import ValidationError
    from django.core.validators import validate_email as django_validate_email

    try:
        django_validate_email(email)
        return True
    except ValidationError:
        return False

