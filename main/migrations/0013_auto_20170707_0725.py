# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170707_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b'static/images/znakZap.jpg'),
        ),
    ]
