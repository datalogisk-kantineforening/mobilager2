# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('quantity', models.PositiveIntegerField()),
                ('delta', models.IntegerField()),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('event', models.ForeignKey(to='inventory.Event')),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tag', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('discontinued', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.IntegerField(default=0, choices=[(0, 'Sellable'), (1, 'Refundable')])),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(serialize=False, max_length=255, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(to='inventory.Vendor'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='inventory.EventType'),
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
