# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anonymizer', '0010_connectionaccesskey'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionaccesskey',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
