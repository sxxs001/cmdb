# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0085_auto_20161208_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='recover',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
