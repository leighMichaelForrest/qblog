# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 02:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180202_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='models',
            new_name='tags',
        ),
    ]