# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20151117_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='tag',
            field=models.CharField(max_length=20, default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='change',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
