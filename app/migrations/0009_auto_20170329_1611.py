# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-03-29 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170327_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='carImage',
            field=models.ImageField(blank=True, null=True, upload_to='driver/'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driversLicence',
            field=models.ImageField(blank=True, null=True, upload_to='driver/'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='drivingLicence',
            field=models.ImageField(blank=True, null=True, upload_to='driver/'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='headPortrait',
            field=models.ImageField(blank=True, null=True, upload_to='driver/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='finishTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderTime',
            field=models.DateTimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='recevingTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transportTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
