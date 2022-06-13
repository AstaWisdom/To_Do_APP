from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null='')
    first_name = models.CharField(max_length=30, blank=True, null='')
    last_name = models.CharField(max_length=50, blank=True, null='')
    email = models.CharField(max_length=200, help_text='Email for Reminders')
    phone = models.CharField(max_length=20, blank=True, null='')
    Email_Reminder = models.BooleanField(default=True, null=False, help_text='Remind Email')
    user_pic = models.ImageField(default='profile-42914.png', null='')

    objects = models.Manager()

    def __str__(self):
        return self.user.username
