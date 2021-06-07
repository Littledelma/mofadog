# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 16:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_order',
            name='dead_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 16, 22, 1, 719840, tzinfo=utc), verbose_name='daed_date'),
        ),
        migrations.AlterField(
            model_name='history_order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 16, 22, 1, 719662, tzinfo=utc), verbose_name='order date'),
        ),
        migrations.AlterField(
            model_name='history_order',
            name='valid_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 16, 22, 1, 719758, tzinfo=utc), verbose_name='valid_date'),
        ),
    ]
