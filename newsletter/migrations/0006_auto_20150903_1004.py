# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20150903_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
