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
                ('good_ptr', models.OneToOneField(auto_created=True, to='core.Good', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=('core.good',),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
