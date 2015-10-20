# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20150903_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 3, 8, 59, 35, 191199, tzinfo=utc)),
        ),
    ]
