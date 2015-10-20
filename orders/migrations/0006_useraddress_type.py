# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20151007_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='type',
            field=models.CharField(default='billing', choices=[('billing', 'Billing'), ('delivery', 'Delivery')], max_length=120),
            preserve_default=False,
        ),
    ]
