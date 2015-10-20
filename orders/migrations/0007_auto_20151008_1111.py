# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_useraddress_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='state',
            new_name='county',
        ),
    ]
