# Generated by Django 3.2.6 on 2021-08-19 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
    ]