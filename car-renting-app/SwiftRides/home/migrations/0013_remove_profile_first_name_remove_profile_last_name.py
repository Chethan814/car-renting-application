# Generated by Django 5.0.1 on 2024-03-26 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_customuser_profile_email_profile_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]