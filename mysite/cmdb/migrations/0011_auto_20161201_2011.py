# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20161201_2007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeptInfo',
            new_name='Dept',
        ),
    ]
