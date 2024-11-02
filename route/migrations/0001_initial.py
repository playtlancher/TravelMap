# Generated by Django 5.1.1 on 2024-10-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]