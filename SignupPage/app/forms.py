from django import forms
from django.forms import ModelForm
from . models import Person

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'something@domain.com'}),
        }
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password didn't match, Please enter your Password again"
            )

class LoginForm(ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'something@domain.com'}))
    class Meta:
        model = Person
        fields = [
            "email",
            "password"
        ]
        widgets = {
            'password': forms.PasswordInput,
        }


