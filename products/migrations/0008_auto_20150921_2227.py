# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150921_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategories',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductCategories',
        ),
    ]
