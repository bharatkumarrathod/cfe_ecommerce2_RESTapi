# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20151008_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(max_digits=50, decimal_places=2, default=0.0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(max_digits=50, decimal_places=2, default=0.0),
        ),
    ]
