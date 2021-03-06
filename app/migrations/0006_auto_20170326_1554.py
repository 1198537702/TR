# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-03-26 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170326_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additionalDemand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='driverId',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='evaluation',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='finishTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderStatus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderTime',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='recevingTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
