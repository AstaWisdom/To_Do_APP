# Generated by Django 3.1.1 on 2020-09-18 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null='')),
                ('first_name', models.CharField(blank=True, max_length=30, null='')),
                ('last_name', models.CharField(blank=True, max_length=50, null='')),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=20, null='')),
                ('Email_Reminder', models.BooleanField(blank=True, null='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
