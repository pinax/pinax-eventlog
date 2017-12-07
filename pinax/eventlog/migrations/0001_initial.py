# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('action', models.CharField(max_length=50, db_index=True)),
                ('extra', jsonfield.fields.JSONField(default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
