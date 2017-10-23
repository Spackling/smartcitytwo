# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 06:35
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
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
                ('username', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')])),
                ('dob', models.DateField(max_length=8)),
                ('address', models.CharField(max_length=100)),
                ('state', models.IntegerField(choices=[(1, 'QLD'), (2, 'NSW'), (3, 'ACT'), (4, 'VIC'), (5, 'SA'), (6, 'WA'), (7, 'NT'), (8, 'TAS')])),
                ('postcode', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)])),
                ('userType', models.IntegerField(choices=[(1, 'student'), (2, 'businessman'), (3, 'tourist')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
