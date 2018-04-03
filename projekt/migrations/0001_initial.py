# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-03 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_firmy', models.CharField(max_length=100)),
                ('branza', models.CharField(max_length=200)),
                ('lokalizacja', models.CharField(max_length=100)),
                ('wakat', models.CharField(max_length=100)),
                ('wynagrodzenie', models.FloatField()),
                ('opis', models.TextField()),
                ('data_utworzenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]