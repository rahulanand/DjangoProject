from django.shortcuts import render
from . forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.set_password(user.password)
            user.save()

            return HttpResponseRedirect('login')
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('success')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def success(request):
    return render(request, 'success.html')