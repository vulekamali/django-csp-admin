# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csp_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cspdirective',
            options={'ordering': ('name',), 'verbose_name': 'CSP Directive'},
        ),
        migrations.AlterField(
            model_name='cspdirectivevalue',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
