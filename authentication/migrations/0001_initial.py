# Generated by Django 5.0.3 on 2024-04-11 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('etablissement', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=128)),
                ('speciality', models.CharField(max_length=32)),
                ('review_number', models.IntegerField()),
                ('review_score', models.IntegerField()),
                ('isMale', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=128)),
                ('isMale', models.BooleanField()),
                ('level', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewsProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_score', models.IntegerField()),
                ('date', models.DateField()),
                ('user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprof')),
            ],
        ),
    ]
