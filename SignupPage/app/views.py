from django.shortcuts import render
from . forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django import forms
from . models import Person
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return HttpResponseRedirect('success')
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
