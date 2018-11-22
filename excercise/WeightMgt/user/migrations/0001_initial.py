# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('login_ip', models.CharField(max_length=100)),
                ('login_time', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('birth', models.DateField()),
                ('height', models.FloatField()),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
    ]
