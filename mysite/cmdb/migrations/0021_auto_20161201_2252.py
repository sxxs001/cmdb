# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0020_provider_providerissue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='dept_status',
            field=models.CharField(choices=[('T', '\u6b63\u5e38'), ('F', '\u5f02\u5e38')], default='T', max_length=255, verbose_name='\u90e8\u95e8\u72b6\u6001'),
        ),
    ]
