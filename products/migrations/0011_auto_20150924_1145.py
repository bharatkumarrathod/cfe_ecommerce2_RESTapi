# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150922_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={'ordering': ['sale_price']},
        ),
    ]
