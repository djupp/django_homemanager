# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='conversion',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=4),
        ),
    ]
