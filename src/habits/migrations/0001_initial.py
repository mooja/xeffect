# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.CharField(unique=True, max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=49)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
