# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
