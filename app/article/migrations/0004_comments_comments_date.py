# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20141211_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
