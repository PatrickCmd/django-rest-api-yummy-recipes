# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180812_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='comment',
        ),
    ]