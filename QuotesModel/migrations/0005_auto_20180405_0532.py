# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuotesModel', '0004_auto_20180405_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='dateofday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
