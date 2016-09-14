# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0003_annresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='KalmanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.FloatField(blank=True, null=True)),
                ('iterations', models.IntegerField(blank=True, null=True)),
                ('seconds', models.IntegerField(blank=True, null=True)),
                ('initial_guess', models.IntegerField(blank=True, null=True)),
                ('truevalue', models.FloatField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]