# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0030_brandmodel_modelconf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelconf',
            name='brand_model',
        ),
        migrations.DeleteModel(
            name='BrandModel',
        ),
        migrations.DeleteModel(
            name='ModelConf',
        ),
    ]
