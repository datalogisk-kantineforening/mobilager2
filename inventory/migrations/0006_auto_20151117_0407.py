# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20151113_0459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date', 'time']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AlterField(
            model_name='change',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
