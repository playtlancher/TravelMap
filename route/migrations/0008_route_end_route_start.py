# Generated by Django 5.1.1 on 2024-11-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0007_remove_route_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='end',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='route',
            name='start',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
