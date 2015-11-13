# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151112_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('delta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('name', models.ForeignKey(to='inventory.User')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='product',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='discontinued',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.AddField(
            model_name='change',
            name='event',
            field=models.ForeignKey(to='inventory.Event'),
        ),
        migrations.AddField(
            model_name='change',
            name='product',
            field=models.ForeignKey(to='inventory.Product'),
        ),
    ]
