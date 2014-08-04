# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('factor', models.DecimalField(decimal_places=1, verbose_name='Conversion factor', max_digits=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('inStore', models.DecimalField(decimal_places=1, verbose_name='Amount of Good in Storage', max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Unit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='good',
            name='defaultUnit',
            field=models.ForeignKey(blank=True, to='core.Measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='toUnit',
            field=models.ForeignKey(to='core.Measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='fromUnit',
            field=models.ForeignKey(to='core.Measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurement',
            name='compatibleUnit',
            field=models.ManyToManyField(through='core.Conversion', to='core.Measurement', blank=True),
            preserve_default=True,
        ),
    ]
