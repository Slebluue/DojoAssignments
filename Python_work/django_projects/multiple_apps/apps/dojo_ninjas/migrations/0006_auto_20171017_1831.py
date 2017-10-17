# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-17 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0005_auto_20171017_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.Dojo'),
        ),
    ]
