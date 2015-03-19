# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0005_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
    ]
