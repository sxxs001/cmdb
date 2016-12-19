# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmrand', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u54c1\u724c')),
                ('bmrandmodel', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u578b\u53f7')),
                ('bmmemo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u54c1\u724c\u578b\u53f7',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u54c1\u724c\u578b\u53f7',
            },
        ),
        migrations.CreateModel(
            name='CommInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DeptInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u90e8\u95e8\u540d\u79f0')),
                ('dept_ownername', models.CharField(blank=True, help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, null=True, verbose_name='\u90e8\u95e8\u8d1f\u8d23\u4eba\u59d3\u540d')),
                ('dept_ownerid', models.CharField(blank=True, help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, null=True, verbose_name='\u90e8\u95e8\u8d1f\u8d23\u4eba\u5de5\u53f7')),
                ('dept_owneremail', models.EmailField(blank=True, help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a&\u62fc\u5199\u68c0\u67e5', max_length=254, null=True, verbose_name='\u90e8\u95e8\u8d1f\u8d23\u4eba\u90ae\u7bb1\u5730\u5740')),
                ('dept_status', models.CharField(choices=[('T', '\u6b63\u5e38'), ('F', '\u5f02\u5e38')], help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u90e8\u95e8\u72b6\u6001')),
                ('memo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u90e8\u95e8\u4fe1\u606f',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u90e8\u95e8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='ModelConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcstype', models.CharField(choices=[('1', '\u6807\u914d'), ('2', '\u975e\u6807')], default='1', help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u662f\u5426\u6807\u51c6\u5316\u914d\u7f6e')),
                ('mcmemory', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u5185\u5b58')),
                ('mccpu', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='CPU')),
                ('mcstore', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u5b58\u50a8')),
                ('mcnt', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u7f51\u7edc')),
                ('mcdesc', models.CharField(help_text='\u53ef\u9009', max_length=255, verbose_name='\u63cf\u8ff0')),
                ('mcmemorybench', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5185\u5b58\u6027\u80fd')),
                ('mccpubench', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='CPU\u6027\u80fd')),
                ('mcstorebench', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5b58\u50a8/IOPS\u6027\u80fd')),
                ('mcntbench', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u7f51\u7edc/PPS\u6027\u80fd')),
                ('mcmemo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
                ('mmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mmodel', to='cmdb.BrandModel', verbose_name='\u54c1\u724c\u578b\u53f7')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u4e3b\u673a\u673a\u578b\u914d\u7f6e',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u4e3b\u673a\u673a\u578b\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u53d1\u884c\u7248')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystemVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_version', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u5c0f\u7248\u672c')),
                ('memo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, verbose_name='\u5907\u6ce8')),
                ('osname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OperatingSystem_Version', to='cmdb.OperatingSystem')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u64cd\u4f5c\u7cfb\u7edf\u53d1\u884c\u7248',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u64cd\u4f5c\u7cfb\u7edf\u53d1\u884c\u7248',
            },
        ),
        migrations.CreateModel(
            name='PrartType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u914d\u4ef6\u7c7b\u578b')),
                ('pmemo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u914d\u4ef6\u7c7b\u578b',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u914d\u4ef6\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(choices=[('1', '\u516c\u6709\u4e91'), ('2', '\u8d1f\u8f7d\u5747\u8861'), ('3', '\u5e26\u5bbd'), ('4', '\u670d\u52a1\u5668'), ('5', '\u4e13\u7ebf'), ('6', '\u4ea4\u6362\u673a'), ('7', '\u9632\u706b\u5899'), ('8', 'IDC'), ('9', '\u5b58\u50a8'), ('10', '\u5b89\u5168'), ('11', '\u7cfb\u7edf\u96c6\u6210&OA')], default='1', help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u4f9b\u5e94\u5546\u7c7b\u522b')),
                ('pcname', models.CharField(help_text='\u4f9b\u5e94\u5546', max_length=255, verbose_name='\u4f9b\u5e94\u5546\u516c\u53f8')),
                ('poname', models.CharField(max_length=255, verbose_name='\u4f9b\u5e94\u5546\u8d1f\u8d23\u4eba')),
                ('pmbnum', models.IntegerField(verbose_name='\u4f9b\u5e94\u5546\u624b\u673a')),
                ('ptelnum', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u4f9b\u5e94\u5546\u5ea7\u673a')),
                ('pcooperate', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u4f9b\u5e94\u5546\u7d27\u5bc6\u5ea6')),
                ('pmemo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u4f9b\u5e94\u5546',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u4f9b\u5e94\u5546',
            },
        ),
        migrations.CreateModel(
            name='ProviderIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pistype', models.CharField(choices=[('1', 'NOC\u5e73\u53f0'), ('2', '\u76d1\u63a7\u544a\u8b66\u5e73\u53f0'), ('3', '\u81ea\u52a8\u53d1\u73b0'), ('4', '\u4eba\u5de5\u53d1\u73b0'), ('5', '\u5176\u4ed6\u4e0a\u62a5\u6e20\u9053')], default='5', help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u95ee\u9898\u6765\u6e90\u6e20\u9053')),
                ('pistartdate', models.DateTimeField(default=django.utils.timezone.now, max_length=255, verbose_name='\u95ee\u9898\u53d1\u751f\u65f6\u95f4')),
                ('pitype', models.CharField(choices=[('1', '\u670d\u52a1\u6545\u969c'), ('2', '\u786c\u4ef6\u6545\u969c'), ('3', '\u8f6f\u4ef6\u6545\u969c'), ('4', '\u670d\u52a1\u6545\u969c'), ('5', '\u5176\u4ed6\u6545\u969c')], default='2', help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, verbose_name='\u6545\u969c\u5206\u7c7b')),
                ('piremark', models.TextField(max_length=1000, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('pisolution', models.TextField(blank=True, max_length=1000, null=True, verbose_name='\u89e3\u51b3\u65b9\u6848')),
                ('piprogress', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u89e3\u51b3\u8fdb\u5ea6')),
                ('pienddate', models.DateTimeField(blank=True, max_length=255, null=True, verbose_name='\u95ee\u9898\u89e3\u51b3\u65f6\u95f4')),
                ('pimemo', models.CharField(blank=True, help_text='\u53ef\u9009', max_length=255, null=True, verbose_name='\u5907\u6ce8')),
                ('piname', models.ForeignKey(help_text='\u4f9b\u5e94\u55461', on_delete=django.db.models.deletion.CASCADE, related_name='Provider_Name', to='cmdb.Provider', verbose_name='\u4f9b\u5e94\u5546')),
            ],
            options={
                'verbose_name': '/\u5143\u6570\u636e/\u4f9b\u5e94\u5546\u95ee\u9898',
                'verbose_name_plural': '/\u5143\u6570\u636e/\u4f9b\u5e94\u5546\u95ee\u9898',
            },
        ),
    ]
