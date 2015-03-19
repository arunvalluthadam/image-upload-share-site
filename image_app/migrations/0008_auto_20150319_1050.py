# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0007_auto_20150319_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ForeignKey(blank=True, to='image_app.Item', null=True),
            preserve_default=True,
        ),
    ]
