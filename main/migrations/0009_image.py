# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('image', models.FileField(blank=True, null=True, upload_to=b'images')),
            ],
        ),
    ]
