# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20141211_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes_table',
            name='likes_for',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='likes_table',
            name='likes_from',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
