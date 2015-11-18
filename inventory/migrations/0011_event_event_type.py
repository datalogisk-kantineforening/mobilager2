# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20151118_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(default=2, to='inventory.EventType'),
            preserve_default=False,
        ),
    ]
