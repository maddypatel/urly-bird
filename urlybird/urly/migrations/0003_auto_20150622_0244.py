# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0002_bookmark_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='shorturl',
            field=models.CharField(max_length=8),
        ),
    ]
