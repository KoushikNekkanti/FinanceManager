from django.shortcuts import render,HttpResponse
from .models import *
from .urls import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.
def home(request):
    return HttpResponse('Hello')