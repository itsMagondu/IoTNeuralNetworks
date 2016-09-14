# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0002_auto_20160907_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.FloatField(blank=True, null=True)),
                ('epochs', models.IntegerField(blank=True, null=True)),
                ('seconds', models.IntegerField(blank=True, null=True)),
                ('hidden_layer_size', models.IntegerField(blank=True, null=True)),
                ('truevalue', models.FloatField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]