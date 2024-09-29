from django.shortcuts import render,redirect
from .models import *
from .urls import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.
def home(request):
    print('kk')
    if request.method =='POST':
        print(request.POST)
        if 'signup_username' in request.POST:
            username = request.POST.get('signup_username')
            email = request.POST.get('signup_email')
            password = request.POST.get('signup_password')
            print('hello')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('/')
            
          
            user = User.objects.create_user(username=username, email=email, password=password)
            user.username=username
            user.email=email
            user.is_active=True
            user.save()
            messages.success(request, 'Account created successfully! Please sign in.')
            return redirect('/')   
            
        elif 'Username' in request.POST:
             
            username=request.POST.get('Username')
            password =request.POST.get('signin_password')
            print(username,password)
            user=authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print('hh')
                login(request, user)
                return redirect('/dashboard')   
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('/')  
    return render(request, 'index.html')
def dashboard(request):
        if request.user.is_authenticated:
               return render(request,'dash.html')
        else:
               return redirect('home')