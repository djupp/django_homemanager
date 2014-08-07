# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(to='core.Unit', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='measurement',
        ),
    ]
