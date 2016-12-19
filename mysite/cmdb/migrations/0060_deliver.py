# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0059_auto_20161206_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField(default=django.utils.timezone.now, help_text='\u9ed8\u8ba4\u503c\u5f53\u524d\u65f6\u95f4,\u53ef\u81ea\u884c\u9009\u62e9', max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('type', models.CharField(choices=[('1', '\u65b0\u589e'), ('2', '\u6269\u5bb9')], default='1', max_length=255, verbose_name='\u9700\u6c42\u7c7b\u578b')),
                ('count', models.IntegerField(verbose_name='\u7533\u8bf7\u6570\u91cf')),
                ('status', models.CharField(choices=[('1', '\u4ea4\u4ed8\u5b8c\u6210'), ('2', '\u6269\u5bb9'), ('3', '\u5f85\u91c7\u8d2d'), ('4', '\u91c7\u8d2d\u4e2d'), ('5', '\u5f85\u4ea4\u4ed8'), ('6', '\u4ea4\u4ed8\u4e2d')], default='3', max_length=255, verbose_name='\u72b6\u6001')),
                ('expect_date', models.DateTimeField(default=django.utils.timezone.now, help_text='\u9ed8\u8ba4\u503c\u5f53\u524d\u65f6\u95f4,\u53ef\u81ea\u884c\u9009\u62e9', max_length=255, verbose_name='\u671f\u5f85\u4ea4\u4ed8\u65f6\u95f4')),
                ('actual_date', models.DateTimeField(default=django.utils.timezone.now, help_text='\u9ed8\u8ba4\u503c\u5f53\u524d\u65f6\u95f4,\u53ef\u81ea\u884c\u9009\u62e9', max_length=255, verbose_name='\u5b9e\u9645\u4ea4\u4ed8\u65f6\u95f4')),
                ('memo', models.TextField(default='\u8bc4\u5ba1\u5355\u53f7:\n\u7533\u8bf7\u5355\u53f7:\n\u4e3b\u673a\u540d:\n\u5176\u4ed6:\n ', max_length=255, verbose_name='\u5907\u6ce8')),
                ('applicant_cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_staff_cname', to='cmdb.Staff', verbose_name='\u7533\u8bf7\u4eba')),
                ('applicant_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_dept', to='cmdb.Dept', verbose_name='\u7533\u8bf7\u90e8\u95e8')),
                ('applicant_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_staff_no', to='cmdb.Staff', verbose_name='\u7533\u8bf7\u4eba\u5de5\u53f7')),
                ('brandmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brandmodel', to='cmdb.BrandModel', verbose_name='\u914d\u7f6e\u7f16\u53f7')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idc', to='cmdb.Idc', verbose_name='\u673a\u623f')),
                ('use_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_dept', to='cmdb.Dept', verbose_name='\u4f7f\u7528\u90e8\u95e8')),
                ('use_deptowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_dept_owner', to='cmdb.Dept', verbose_name='\u4f7f\u7528\u90e8\u95e8\u8d1f\u8d23\u4eba')),
                ('use_names', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_staff_cnames', to='cmdb.Staff', verbose_name='\u4f7f\u7528\u4eba')),
            ],
            options={
                'verbose_name': '/Meta/\u4e3b\u673a\u4ea4\u4ed8',
                'verbose_name_plural': '/Meta/\u4e3b\u673a\u4ea4\u4ed8',
            },
        ),
    ]
