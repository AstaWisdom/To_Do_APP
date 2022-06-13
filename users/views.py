from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import SignupForm, UserProfileForm, ProfilePicture
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import UserProfile
from learning_logs.email import user_emails


def user_email_sending(user_email, add=False):

    if add:
        user_emails.append(user_email)
    elif user_email not in user_emails:
        pass
    else:
        user_emails.remove(user_email)

# Create your views here.


def register(request):
    """Register new user"""
    if request.method != 'POST':
        # display a blank registration
        form = SignupForm()
    else:
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password, email=email)
            # login the user and redirect to the home page
            login(request, user)
            return redirect('learning_logs:index')

    # display a blank page
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def user_profile(request, user_id):
    """Edit the user profile"""
    user = User.objects.get(id=user_id)
    try:
        profile = UserProfile.objects.get(user=user)
    except :
        profile = UserProfile(user=request.user)

    if request.method != 'POST':
        # Display the form
        form = UserProfileForm(instance=profile)

    else:
        form = UserProfileForm(data=request.POST, instance=profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = user
            user.email = form.cleaned_data.get('email')

            if form.cleaned_data.get('Email_Reminder'):
                user_email_sending(user.email, True)
            else:
                user_email_sending(user.email, False)

            user_profile.save()
            messages.success(request, 'Your Profile Updated.')

            return redirect('users:user_profile', user.id)

    context = {'form': form, }
    return render(request, 'registration/user_profile.html', context)

@login_required
def profile_picture(request, user_id):
    user = User.objects.get(id=user_id)
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        profile = UserProfile(user=request.user)

    if request.method != 'POST':
        # Display the form
        form = ProfilePicture(instance=profile)

    else:
        form = ProfilePicture(data=request.POST, files=request.FILES, instance=profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.user_pic = form.files.get('user_pic')
            user_profile.save()

            messages.success(request, 'Your Photo Updated.')

            return redirect('users:profile_picture', user.id)

    context = {'form': form}
    return render(request, 'registration/profile_picture.html', context)