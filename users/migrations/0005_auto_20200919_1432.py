# Generated by Django 3.1.1 on 2020-09-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200919_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_pic',
            field=models.ImageField(blank=True, null='', upload_to='profile_image'),
        ),
    ]
