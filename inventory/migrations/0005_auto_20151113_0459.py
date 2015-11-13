# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20151113_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtype',
            old_name='description',
            new_name='name',
        ),
        migrations.AddField(
            model_name='change',
            name='confirmed',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
    ]
