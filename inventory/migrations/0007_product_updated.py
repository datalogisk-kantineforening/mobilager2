# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20151117_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 17, 4, 53, 40, 246253, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
