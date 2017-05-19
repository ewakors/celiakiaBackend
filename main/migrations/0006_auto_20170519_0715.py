# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-19 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170519_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b'product_images'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b'category_images'),
        ),
    ]
