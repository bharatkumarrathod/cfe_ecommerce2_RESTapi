# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150821_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
