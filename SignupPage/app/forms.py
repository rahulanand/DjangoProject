from django import forms
from django.forms import ModelForm
from . models import Person

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    class Meta:
        model = Person
        fields = '__all__'


