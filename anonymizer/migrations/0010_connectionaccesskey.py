# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anonymizer', '0009_connectionconfiguration_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionAccessKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('key', models.TextField()),
                ('last_used', models.DateTimeField(default=None, null=True, blank=True)),
                ('connection', models.ForeignKey(related_name='access_keys', to='anonymizer.ConnectionConfiguration')),
            ],
        ),
    ]
