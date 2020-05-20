# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

try:
    import jsonfield.fields
    field = jsonfield.fields.JSONField(default=dict)
except ImportError:
    field = models.TextField()

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
                ('extra', field),
                ('user', models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
