# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0019_auto_20170905_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='system_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.system_users', verbose_name='登陆用户'),
        ),
    ]
