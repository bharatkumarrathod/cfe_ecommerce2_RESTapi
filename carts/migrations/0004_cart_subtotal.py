# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_line_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(max_digits=50, decimal_places=2, default=0.0),
            preserve_default=False,
        ),
    ]
