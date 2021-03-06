# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securities', '0003_bond_exchangetradedfund_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangetradedfund',
            name='alpha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchangetradedfund',
            name='beta',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchangetradedfund',
            name='r_squared',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exchangetradedfund',
            name='sharpe_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
