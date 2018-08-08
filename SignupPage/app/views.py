from django.shortcuts import render
from . forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django import forms
from . models import Person
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                if validate_password(password, password_validators=None) == None:
                    user.set_password(password)
                    user.save()
                    return HttpResponseRedirect('success')
            except 	ValidationError:
                messages.error(request, "Please Enter a Strong Password, contains 8 Characters and !@#$%^&*() ")

    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        obj = Person.objects.get(email=username)
        if check_password(password, obj.password):
            user = authenticate(request, username=username, password= password)
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return HttpResponseRedirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.error(request,"Invalid Credentials")
    else:
        form = LoginForm()   
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def home_view(request):
    return render(request, 'home.html')
