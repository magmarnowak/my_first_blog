# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]