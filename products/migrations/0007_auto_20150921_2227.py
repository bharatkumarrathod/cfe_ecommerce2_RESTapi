# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_productcategories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategories',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='productcategories',
            name='default',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(to='products.Category', related_name='default_category', null=True, blank=True),
        ),
    ]
