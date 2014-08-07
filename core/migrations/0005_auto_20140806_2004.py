# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20140806_2004'),
        ('cooking', '0002_auto_20140806_2004'),
        ('core', '0004_auto_20140806_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversion',
            name='fromMeasurement',
        ),
        migrations.RemoveField(
            model_name='conversion',
            name='toMeasurement',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='relatedMeasurements',
        ),
        migrations.DeleteModel(
            name='Conversion',
        ),
        migrations.AddField(
            model_name='good',
            name='defaultUnit',
            field=models.ForeignKey(to='core.Unit', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='good',
            name='defaultMeasurement',
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
    ]
