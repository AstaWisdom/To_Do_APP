# Generated by Django 3.1.1 on 2020-09-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200919_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_pic',
            field=models.ImageField(default='djangoProject/images/profile-42914.png', null='', upload_to=''),
        ),
    ]
