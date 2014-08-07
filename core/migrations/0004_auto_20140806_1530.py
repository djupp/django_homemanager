# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_unit_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='conversion',
            field=models.DecimalField(decimal_places=10, max_digits=20, default=1),
        ),
    ]
