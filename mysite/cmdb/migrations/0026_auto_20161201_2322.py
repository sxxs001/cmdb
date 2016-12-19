# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0025_auto_20161201_2317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prarttype',
            options={'verbose_name': '/Meta/\u914d\u4ef6\u7c7b\u578b', 'verbose_name_plural': '/Meta/\u914d\u4ef6\u7c7b\u578b'},
        ),
        migrations.RemoveField(
            model_name='prarttype',
            name='pmemo',
        ),
        migrations.RemoveField(
            model_name='prarttype',
            name='ptype',
        ),
        migrations.AddField(
            model_name='prarttype',
            name='memo',
            field=models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AddField(
            model_name='prarttype',
            name='type',
            field=models.CharField(default='a', help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u914d\u4ef6\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]
