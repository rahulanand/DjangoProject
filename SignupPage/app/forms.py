from django import forms
from django.forms import ModelForm
from . models import Person

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'something@domain.com'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    #q = forms.CharField(label='search', 
    #                widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    #first_name = forms.CharField(label='First Name')
    class Meta:
        model = Person
        fields = '__all__'

class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'something@domain.com'}))
    class Meta:
        model = Person
        fields = [
            "email",
            "password"
        ]


