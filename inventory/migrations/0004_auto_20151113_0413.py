# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20151113_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='other_name',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AddField(
            model_name='eventname',
            name='event',
            field=models.ForeignKey(to='inventory.Event'),
        ),
        migrations.AddField(
            model_name='eventname',
            name='name',
            field=models.ForeignKey(to='inventory.User'),
        ),
    ]
