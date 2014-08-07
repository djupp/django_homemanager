# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='unit',
            field=models.ForeignKey(to='core.Unit'),
        ),
    ]
