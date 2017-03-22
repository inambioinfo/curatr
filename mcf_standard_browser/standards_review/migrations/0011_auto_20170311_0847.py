# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-11 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards_review', '0010_renameMCFID_massBankRequisits'),
    ]

    operations = [
        migrations.AddField(
            model_name='fragmentationspectrum',
            name='_splash',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='ion_analyzer',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='ionization_method',
            field=models.TextField(default=''),
        ),
    ]
