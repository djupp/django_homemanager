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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('factor', models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Conversion factor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('inStore', models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Amount of Good in Storage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='good',
            name='defaultMeasurement',
            field=models.ForeignKey(to='core.Measurement', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='toMeasurement',
            field=models.ForeignKey(to='core.Measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='fromMeasurement',
            field=models.ForeignKey(to='core.Measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurement',
            name='relatedMeasurements',
            field=models.ManyToManyField(to='core.Measurement', blank=True, through='core.Conversion'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('conversion', models.DecimalField(max_digits=10, blank=True, decimal_places=4)),
                ('baseUnit', models.ForeignKey(to='core.Unit', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
