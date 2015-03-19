# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0006_auto_20150319_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True)),
                ('content', models.TextField(null=True, verbose_name='Designation', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='comments',
            field=models.ForeignKey(blank=True, to='image_app.Comments', null=True),
            preserve_default=True,
        ),
    ]
