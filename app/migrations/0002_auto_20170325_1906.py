# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-03-25 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contactsName',
            field=models.CharField(default='mike', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='contactsTell',
            field=models.CharField(default='110', max_length=11),
            preserve_default=False,
        ),
    ]
