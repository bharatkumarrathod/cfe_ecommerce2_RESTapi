# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20150821_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 3, 8, 53, 29, 260610, tzinfo=utc)),
        ),
    ]
