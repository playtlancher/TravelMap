# Generated by Django 5.1.1 on 2024-11-02 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_route_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='tags',
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='route.route')),
            ],
        ),
    ]