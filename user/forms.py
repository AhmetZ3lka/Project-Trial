from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 20, min_length = 4, label=(" User Name "))
    password = forms.CharField(max_length = 25, min_length = 5, label=("PassWord"),widget=forms.PasswordInput)
    confirm = forms.CharField(max_length = 25, min_length = 5, label=("Confirm The PassWord"),widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError(" Passwords are not same. ")

        values = {
            "username" : username,
            "password" : password
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label = "User Name")
    password = forms.CharField(label = "Password",widget=forms.PasswordInput)