from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth.models import User


user_emails = []


# Send email every day to the users to see their schedule of the day
active = False
while active:
    # Get the time
    now = datetime.now()
    # Format the time and save it
    time_sending = now.strftime('%H:%M:%S')
    if time_sending == '07:00:00':
        for user_email in user_emails:
            send_mail('Your Notes', 'Check the schedule!', 'notesinkeep@gmail.com', [user_email], fail_silently=False)
