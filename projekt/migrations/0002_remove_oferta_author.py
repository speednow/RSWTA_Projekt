# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-03 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='author',
        ),
    ]