from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django import forms


class Signup_Form(UserCreationForm,forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=User
        fields=['username','password1','password2']

class Login_form(forms.Form):
    captcha = CaptchaField()