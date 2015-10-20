# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 21, 21, 38, 31, 813512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
