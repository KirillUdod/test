# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20141211_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thubnail',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=True,
        ),
    ]
