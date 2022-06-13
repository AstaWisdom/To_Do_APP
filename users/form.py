from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=1, help_text='* at least 1 characters')
    email = forms.CharField(max_length=200, help_text='example@gmail.com')

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'phone', 'email', 'Email_Reminder']


class ProfilePicture(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_pic']