# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_event_event_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='other_name',
        ),
    ]
