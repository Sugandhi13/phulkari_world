# Generated by Django 3.2.3 on 2024-06-10 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20240610_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
    ]
