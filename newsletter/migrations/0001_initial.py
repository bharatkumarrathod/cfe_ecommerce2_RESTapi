# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=255, blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 21, 21, 31, 24, 814886, tzinfo=utc))),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
