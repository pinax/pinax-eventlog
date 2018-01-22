# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('eventlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='log',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
