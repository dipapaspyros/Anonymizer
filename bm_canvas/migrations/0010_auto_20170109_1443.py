# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_canvas', '0009_auto_20170109_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessmodel',
            name='palette_config',
            field=models.TextField(default=b'{"67809F": "Pending approval", "F89406": "Idea", "65C6BB": "Innovation", "6C7A89": "Design", "BDC3C7": "Testing", "333": "Competitive advantage", "333333": "Competitive advantage", "E9D460": "Blocking", "1BBC9B": "Complete", "7D3C8C": "Main action", "EF4836": "Danger", "FFF": "No tag", "FFFFFF": "No tag", "4183D7": "Ongoing"}'),
        ),
    ]
