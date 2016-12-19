# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0031_auto_20161201_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u54c1\u724c')),
                ('brand_model', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u578b\u53f7')),
                ('memo', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/Meta/\u54c1\u724c\u578b\u53f7',
                'verbose_name_plural': '/Meta/\u54c1\u724c\u578b\u53f7',
            },
        ),
        migrations.CreateModel(
            name='ModelConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', '\u6807\u914d'), ('2', '\u975e\u6807')], default='1', max_length=255, verbose_name='\u662f\u5426\u6807\u51c6\u5316\u914d\u7f6e')),
                ('memory', models.CharField(max_length=255, verbose_name='\u5185\u5b58')),
                ('cpu', models.CharField(max_length=255, verbose_name='CPU')),
                ('store', models.CharField(max_length=255, verbose_name='\u5b58\u50a8')),
                ('network', models.CharField(max_length=255, verbose_name='\u7f51\u7edc')),
                ('remark', models.CharField(max_length=255, verbose_name='\u63cf\u8ff0')),
                ('memory_bench', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5185\u5b58\u6027\u80fd')),
                ('cpu_bench', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='CPU\u6027\u80fd')),
                ('store_bench', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5b58\u50a8/IOPS\u6027\u80fd')),
                ('network_bench', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u7f51\u7edc/PPS\u6027\u80fd')),
                ('memo', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
                ('brand_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='cmdb.BrandModel', verbose_name='\u54c1\u724c\u578b\u53f7')),
            ],
            options={
                'verbose_name': '/Meta/\u673a\u578b\u914d\u7f6e',
                'verbose_name_plural': '/Meta/\u673a\u578b\u914d\u7f6e',
            },
        ),
    ]
