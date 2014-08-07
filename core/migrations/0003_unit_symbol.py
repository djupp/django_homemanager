# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140806_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='symbol',
            field=models.CharField(null=True, blank=True, max_length=5),
            preserve_default=True,
        ),
    ]
