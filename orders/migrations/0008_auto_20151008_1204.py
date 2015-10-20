# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20151008_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(max_length=120, choices=[('billing', 'Billing'), ('shipping', 'Shipping')]),
        ),
    ]
