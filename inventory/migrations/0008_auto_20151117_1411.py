# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_product_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='acribe',
            new_name='acrive',
        ),
    ]
