# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0041_auto_20161204_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', '\u6b63\u5e38'), ('2', '\u5f02\u5e38')], default='1', max_length=255, verbose_name='\u4ea7\u54c1\u72b6\u6001')),
                ('product', models.CharField(max_length=255, unique=True, verbose_name='\u4ea7\u54c1')),
                ('memo', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/Meta/\u4ea7\u54c1',
                'verbose_name_plural': '/Meta/\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', '\u6b63\u5e38'), ('2', '\u5f02\u5e38')], default='1', max_length=255, verbose_name='\u4ea7\u54c1\u7ebf\u72b6\u6001')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='\u4ea7\u54c1\u7ebf')),
                ('memo', models.CharField(blank=True, help_text='\u9009\u586b', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/Meta/\u4ea7\u54c1\u7ebf',
                'verbose_name_plural': '/Meta/\u4ea7\u54c1\u7ebf',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.ManyToManyField(related_name='Product_ProductLine', to='cmdb.ProductLine', verbose_name='\u4ea7\u54c1\u7ebf'),
        ),
    ]
