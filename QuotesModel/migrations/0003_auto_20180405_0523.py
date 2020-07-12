# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuotesModel', '0002_auto_20180405_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quotesday',
            field=models.ForeignKey(to='QuotesModel.Days', null=True),
        ),
    ]
