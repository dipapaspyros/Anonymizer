# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anonymizer', '0008_auto_20160111_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionconfiguration',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 29, 14, 59, 11, 520000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
