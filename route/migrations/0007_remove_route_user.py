# Generated by Django 5.1.1 on 2024-11-02 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_route_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='user',
        ),
    ]
