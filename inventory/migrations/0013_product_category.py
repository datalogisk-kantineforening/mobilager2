# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_remove_event_other_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, 'Sellable'), (1, 'Refundable')]),
        ),
    ]
