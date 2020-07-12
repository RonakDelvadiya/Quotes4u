# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuotesModel', '0003_auto_20180405_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quotesday',
            field=models.ForeignKey(blank=True, to='QuotesModel.Days', null=True),
        ),
    ]
