# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0073_auto_20161206_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('1', '\u7b49\u5f85\u4f9b\u5e94\u5546\u53d1\u9001\u5408\u540c\u7535\u5b50\u7248'), ('2', '\u6cd5\u52a1\u5ba1\u6279\u4e2d'), ('3', '\u5feb\u9012\u76d6\u7ae0\u7eb8\u8d28\u5408\u540c\u5236\u4f9b\u5e94\u5546'), ('4', '\u4f9b\u5e94\u5546\u5f55\u5165'), ('5', '\u4f9b\u5e94\u5546\u5165\u5e93'), ('6', '\u4f9b\u5e94\u5546\u4e0b\u5355')], default='3', max_length=255, verbose_name='\u72b6\u6001'),
        ),
    ]
