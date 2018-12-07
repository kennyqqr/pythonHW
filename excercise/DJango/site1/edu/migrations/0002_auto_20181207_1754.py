# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='end',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='start',
        ),
        migrations.AddField(
            model_name='classes',
            name='period',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='classes',
            name='periodend',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='classes',
            name='weekday',
            field=models.IntegerField(default=0),
        ),
    ]
