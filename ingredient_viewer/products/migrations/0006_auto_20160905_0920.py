# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160904_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(help_text='Add ingredients here.', null=True),
        ),
    ]