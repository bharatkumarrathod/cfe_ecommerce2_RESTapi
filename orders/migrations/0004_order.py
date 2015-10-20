# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20151006_1205'),
        ('orders', '0003_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('shipping_total_price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('billing_address', models.ForeignKey(related_name='billing_address', to='orders.UserAddress')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', to='orders.UserAddress')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
