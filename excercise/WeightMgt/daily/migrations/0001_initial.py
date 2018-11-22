# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('weight', models.FloatField()),
                ('bodyfat', models.FloatField()),
                ('innerfat', models.FloatField()),
                ('basal_metabolism', models.IntegerField()),
                ('body_age', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
    ]
