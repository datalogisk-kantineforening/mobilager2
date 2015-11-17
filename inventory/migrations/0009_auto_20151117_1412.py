# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20151117_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='acrive',
            new_name='active',
        ),
    ]
