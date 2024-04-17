from django.shortcuts import render , HttpResponse ,redirect
from firstapp.models import Student , EmailModel
from firstapp.forms import *
from firstapp import forms
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404

def index(request):
    return render ( request , 'home.html')# this is to render the tempplate on home page we can create at any but as this is passed and return by index than it will be passed to home page

@login_required
def student_profile(request):
    # Get the first name of the currently logged-in user
    logged_in_user_first_name = request.user.first_name
    
    # Filter students by the first name
    try:
        student = Student.objects.get(first_name=logged_in_user_first_name)
    except Student.DoesNotExist:
        # If no student found with the first name, raise 404 or handle appropriately
        return render(request, 'student_NAN.html')
    
    context = {
        'student': student,
    }
    return render(request, 'student.html', context)

def about( request):
    return render ( request , 'about.html')

def contact( request):
    return render ( request , 'contact.html')

def memoreis( request):
    return render ( request , 'memories.html')


def registration( request):
    # views.py
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password , first_name=firstname , last_name=lastname)
                user.save()
                login(request, user)
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'registration.html' )



@login_required
def studdetails( request , id ):
    students = Students.objects.get(id=id)
    context = {
        'students' : students ,
    }

    return render ( request , 'studdetail.html' , context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a home page or dashboard
            else:
                message = 'Login failed!'
        else:
            message = 'Please check your inputs.'
    else:
        form = LoginForm()
        message = ''
    return render(request, 'login.html', {'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')

def login_req(request):
    return render ( request , 'login_req.html')

def submit_email(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        EmailModel.objects.create(email=email)
        context['message'] = 'Email submitted successfully!'
    return render(request, 'home.html', context)

def working( request):
    return render ( request , 'workingonit.html')

@login_required
def login_success_view(request):
    return render(request, 'success.html')

def contact_success_view(request ,  first_name):
    return render(request, 'csucc.html' , {'first_name': first_name})

def contact(request ):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            return redirect('csuccess' , first_name=new_contact.first_name)  # Redirect to a new URL if the form is successful
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})