# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20161201_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='id',
        ),
        migrations.AlterField(
            model_name='provider',
            name='pmbnum',
            field=models.FloatField(primary_key='\u4f9b\u5e94\u5546\u624b\u673a', serialize=False, verbose_name=11),
        ),
    ]
