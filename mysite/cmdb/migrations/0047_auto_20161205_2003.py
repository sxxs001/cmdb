# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0046_auto_20161205_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalerror',
            name='conf',
            field=models.TextField(default='\u7f51\u5361bond\u914d\u7f6e:\n cpu\u7701\u7535\u786c\u4ef6\u914d\u7f6e:\n cpu\u7701\u7535\u8f6f\u4ef6\u914d\u7f6e:\n cpu\u8d85\u7ebf\u7a0b:\n bios\u7248\u672c:\n \u6587\u4ef6\u7cfb\u7edfxfs:\n \u865a\u62df\u5316\u8d85\u5206:\n', max_length=255, verbose_name='\u914d\u7f6e\u9879'),
        ),
    ]
