# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b"Author's Name")),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=100, verbose_name=b'Category')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dayname', models.CharField(default=b'', unique=True, max_length=100, verbose_name=b'Day')),
                ('dateofday', models.DateField(null=True)),
                ('dayhistory', models.TextField(default=b'', max_length=100, verbose_name=b'History')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Day',
                'verbose_name_plural': 'Day',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occupation', models.CharField(unique=True, max_length=100, verbose_name=b'Ocuupation')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Occupation',
                'verbose_name_plural': 'Occupation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.CharField(unique=True, max_length=255, verbose_name=b'Quote')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('authorid', models.ForeignKey(verbose_name=b'Select Auther', to='QuotesModel.Author')),
                ('category', models.ManyToManyField(to='QuotesModel.Category', null=True, verbose_name=b'Select Category', blank=True)),
                ('quotesday', models.ForeignKey(default=b'', to='QuotesModel.Days')),
            ],
            options={
                'verbose_name': 'Quotes',
                'verbose_name_plural': 'Quotes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='author',
            name='occupationid',
            field=models.ForeignKey(to='QuotesModel.Occupation'),
            preserve_default=True,
        ),
    ]
