# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20170425_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='options',
            old_name='option1',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='options',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='options',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='options',
            name='option4',
        ),
    ]
