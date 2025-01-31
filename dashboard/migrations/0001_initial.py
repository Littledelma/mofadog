# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('Remark', models.CharField(max_length=50)),
                ('domain_name', models.CharField(max_length=32)),
                ('group', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(default=0)),
                ('sspwd', models.CharField(max_length=32)),
                ('lastConnTime', models.IntegerField(default=0)),
                ('flow_up', models.BigIntegerField(default=0)),
                ('flow_down', models.BigIntegerField(default=0)),
                ('transfer', models.BigIntegerField(default=0)),
                ('enable', models.BooleanField(default=True)),
                ('method', models.CharField(max_length=32)),
                ('plan', models.CharField(max_length=4)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='order date')),
                ('valid_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='valid_date')),
                ('dead_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='daed_date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('answer_text', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
