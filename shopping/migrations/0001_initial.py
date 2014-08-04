# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('good_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='core.Good')),
            ],
            options={
            },
            bases=('core.good',),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=1, max_digits=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit', models.ForeignKey(to='core.Measurement')),
                ('what', models.ForeignKey(to='shopping.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchase',
            name='where',
            field=models.ForeignKey(to='shopping.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ManyToManyField(through='shopping.Purchase', to='shopping.Store'),
            preserve_default=True,
        ),
    ]
