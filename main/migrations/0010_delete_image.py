# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
