# Generated by Django 5.0.1 on 2024-01-19 23:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('time', models.DurationField()),
                ('difficulty', models.CharField(choices=[('very_easy', 'Very easy'), ('easy', 'Easy'), ('medium', 'Medium'), ('advanced', 'Advanced'), ('hard', 'Hard')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('code', models.CharField(max_length=32, unique=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('exercises', models.ManyToManyField(to='tests.exercise')),
            ],
        ),
    ]
