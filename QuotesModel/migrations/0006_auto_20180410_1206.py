# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuotesModel', '0005_auto_20180405_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='occupationid',
            field=models.ForeignKey(blank=True, to='QuotesModel.Occupation', null=True),
        ),
    ]
