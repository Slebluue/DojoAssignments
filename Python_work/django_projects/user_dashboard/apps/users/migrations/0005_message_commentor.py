# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='commentor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
